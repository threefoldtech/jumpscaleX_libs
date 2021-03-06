from nacl.encoding import Base64Encoder

from Jumpscale import j

from .auth import HTTPSignatureAuth
from .pagination import get_all, get_page


class Nodes:
    def __init__(self, client):
        self._client = client
        self._session = self._client._session
        self._model = j.data.schema.get_from_url("tfgrid.directory.node.2")

    def _query(self, farm_id=None, country=None, city=None, cru=None, sru=None, mru=None, hru=None, proofs=False):
        query = {}
        if proofs:
            query["proofs"] = "true"
        args = {
            "farm": farm_id,
            "city": city,
            "cru": cru,
            "sru": sru,
            "mru": mru,
            "hru": hru,
        }
        for k, v in args.items():
            if v is not None:
                query[k] = v
        return query

    def list(
        self, farm_id=None, country=None, city=None, cru=None, sru=None, mru=None, hru=None, proofs=False, page=None
    ):

        query = self._query(farm_id, country, city, cru, sru, mru, hru, proofs)
        url = self._client.url + "/nodes"

        if page:
            nodes, _ = get_page(self._session, page, self._model, url, query)
        else:
            nodes = list(self.iter(farm_id, country, city, cru, sru, mru, hru, proofs))

        return nodes

    def iter(self, farm_id=None, country=None, city=None, cru=None, sru=None, mru=None, hru=None, proofs=False):
        query = self._query(farm_id, country, city, cru, sru, mru, hru, proofs)
        url = self._client.url + "/nodes"
        yield from get_all(self._session, self._model, url, query)

    def get(self, node_id, proofs=False):
        params = {}
        if proofs:
            params["proofs"] = "true"
        resp = self._session.get(self._client.url + f"/nodes/{node_id}", params=params)
        return self._model.new(datadict=resp.json())

    def configure_free_to_use(self, node_id, free, identity=None):
        if not isinstance(free, bool):
            raise j.exceptions.Input("free must be a boolean")

        me = identity if identity else j.me
        secret = me.encryptor.signing_key.encode(Base64Encoder)

        auth = HTTPSignatureAuth(key_id=str(me.tid), secret=secret, headers=["(created)", "date", "threebot-id"])
        headers = {"threebot-id": str(me.tid)}

        data = {"free_to_use": free}
        self._session.post(self._client.url + f"/nodes/{node_id}/configure_free", auth=auth, headers=headers, json=data)
        return True

    def configure_public_config(self, node_id, master_iface, ipv4, gw4, ipv6, gw6, identity=None):
        node = self.get(node_id)

        public_config = node.public_config
        public_config.master = master_iface
        public_config.ipv4 = ipv4
        public_config.gw4 = gw4
        public_config.ipv6 = ipv6
        public_config.gw6 = gw6
        public_config.type = "MACVLAN"
        public_config.version += 1

        me = identity if identity else j.me
        secret = me.encryptor.signing_key.encode(Base64Encoder)

        auth = HTTPSignatureAuth(key_id=str(me.tid), secret=secret, headers=["(created)", "date", "threebot-id"])
        headers = {"threebot-id": str(me.tid)}

        data = public_config._ddict
        self._session.post(self._client.url + f"/nodes/{node_id}/configure_public", auth=auth, headers=headers, json=data)
        return True
