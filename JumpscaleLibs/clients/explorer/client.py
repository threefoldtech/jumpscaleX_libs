from urllib.parse import urlparse

import requests

from Jumpscale import j

from .errors import raise_for_status
from .farms import Farms
from .gateway import Gateway
from .nodes import Nodes
from .reservations import Reservations
from .users import Users

JSConfigClient = j.baseclasses.object_config


class Explorer(JSConfigClient):

    _SCHEMATEXT = """
        @url = tfgrid.explorer.client
        name** = "" (S)
        url = (S)
        """

    def _init(self, **kwargs):
        # load models
        self.url = self.url.rstrip("/")
        self._session = requests.Session()
        self._session.hooks = dict(response=raise_for_status)

        self.nodes = Nodes(self._session, self.url)
        self.users = Users(self._session, self.url)
        self.farms = Farms(self._session, self.url)
        self.reservations = Reservations(self._session, self.url)
        self.gateway = Gateway(self._session, self.url)
