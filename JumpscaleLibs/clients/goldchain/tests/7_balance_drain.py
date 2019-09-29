from Jumpscale import j

from JumpscaleLibs.clients.goldchain.stub.ExplorerClientStub import GoldChainExplorerGetClientStub
from JumpscaleLibs.clients.goldchain.test_utils import cleanup


def main(self):
    """
    to run:

    kosmos 'j.clients.goldchain.test(name="balance_drain")'
    """

    cleanup("devnet_unitttest_client")

    # create a goldchain client for devnet
    c = j.clients.goldchain.new("devnet_unittest_client", network_type="DEV")

    # (we replace internal client logic with custom logic as to ensure we can test without requiring an active network)
    explorer_client = GoldChainExplorerGetClientStub()
    explorer_client.hash_add(
        "000000000000000000000000000000000000000000000000000000000000000000000000000000",
        '{"hashtype":"unlockhash","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"00d1eb537582e31f86a818b32e3a8e10110c1e4348b2d1d0c6746b4b75f3ddc8","height":8887,"parent":"09548093238b2592cc88e0e834a641bf2bcc6fe85275e50d0e179f720a5157c7","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"fb0ce589309af98870f7aa1b620948f8fbca2900d0729bfe1e4f501b45ae87c3","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"d0ff7079fcf804a011c7bfc226a2d9fc3ab07fbe135abbe44ebb81d64a59cb90bd647c48747e305d8af2c13ac04b8e4eb992156beeef3f31a74566684ad0c009"}}}],"coinoutputs":[{"value":"1","condition":{}},{"value":"2999999999","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"4000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["4be59838a2baaf69afbc558e961aae584f69b74ab72321799f380d02d5adea01","1744c053787a5662fad3651c0ed6c68b8bb5584370a81c95aa15cfcf220bfe13"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"040e33a58c70e3f912b0851650ba6708c6e167b05bbe1f15fc5e870e46de435a","height":8830,"parent":"a06da42631ed8bc80ba9b383474172900fa6b804758b2f6d866d95542b4b4a28","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"0846ce4e40bd153f4b24c1131908ba87e2c99d78615c16eaac846cb3ca033562","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"90e6d2c8bb8d5ba7d5edcf38cf87d7ce1ec9d936b6939c05571f5317fd83ba495f895adc8695eedd35087c08f780eff05a74240bf1245eac920971c604892802"}}}],"coinoutputs":[{"value":"1000000000","condition":{}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"2000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["6eb896edab9539b41077a7fb540a4987d5e8b434ec77e150c1e571d2883652f2"],"coinoutputunlockhashes":[""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"3d3ef900a0c54b45430c6248cf7bfbbbf92da663c84b73b10794eb2a9b0a74f5","height":7023,"parent":"e12271a40b3959d64cdf5d3845546c568a7db9313ca7b117a03454469cd6b348","rawtransaction":{"version":129,"data":{"nonce":"kyA3WfkRL6M=","mintfulfillment":{"type":3,"data":{"pairs":[{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"fa5560db80a0dcf7676885cf3517685c18bc82d787337299179d7c06271cbf724ced43d45f7bed7364c89f5adf5231264f322dee8d851606db8fd0494b45960e"}]}},"coinoutputs":[{"value":"1000000000","condition":{}}],"minerfees":["1000000000"],"arbitrarydata":"bW9yZSBmb3IgYWxs"}},"coininputoutputs":null,"coinoutputids":["0ffc3aceee0f3f695d1173056998e49e964c72c6b9d9ce08258f51cce6d9cd18"],"coinoutputunlockhashes":[""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"422ff9ec3d34e263a9eb910c41b4c031e5ff0b8ba9dc5377518e7ed2cfda72ec","height":8872,"parent":"2b465d727d65da5c2986ed8b9b1a3211cd27f7b99f4bc887c801f7bbfb05f884","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"b4c0b5d51891608fc2bf0c93c001325ee5048ffdaf6239bca99b9cf46cbe6932","fulfillment":{"type":3,"data":{"pairs":[{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"7303e9e048ee66def55305fb069d9a75cc15e96168bd85ca102dfdea2c26a4e3776adcae341610e85217508cf24a3a82f711f12286d1de37fc248b375556fd08"},{"publickey":"ed25519:9e310aa31e236f4f1da9c5384138674dc68323da2d8d6cf6e8ee5055b88b61e3","signature":"acd50c4825e639e6423b07022b5b69125ee04014adc6b870e358222dc4a7b2733200ad68aa4f978fba2e306acb06912ae625cfd697f42d9d20bdac3e7faf5f0f"}]}}}],"coinoutputs":[{"value":"42000000000","condition":{}},{"value":"390999999534","condition":{"type":4,"data":{"unlockhashes":["0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab","01822fd5fefd2748972ea828a5c56044dec9a2b2275229ce5b212f926cd52fba015846451e4e46"],"minimumsignaturecount":2}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"433999999534","condition":{"type":4,"data":{"unlockhashes":["0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab","01822fd5fefd2748972ea828a5c56044dec9a2b2275229ce5b212f926cd52fba015846451e4e46"],"minimumsignaturecount":2}},"unlockhash":"03e9dbb15388d815ecb1d898bf94cc60e37053d12c7fe97bba2578c8b6a7dbdfb0b3caff77c6c6"}],"coinoutputids":["170815e3fd93f34e5b40644dd116efcfa27fd3e4f6992a68759978336a16fe5e","8ffb6836d68e12a9eb99b8b312399832cdfcbe461d75c3ceca6256b5afabe29e"],"coinoutputunlockhashes":["","03e9dbb15388d815ecb1d898bf94cc60e37053d12c7fe97bba2578c8b6a7dbdfb0b3caff77c6c6"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"617c2fd23b25a55c688e0cdb97c456b51bda09fdac24bc08e20196c25a3f4f95","height":6825,"parent":"7798fefb7ff9d07672c10028b1e26c1fe44865bbf47c150cb7dabb539dce8cb3","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"d5b4eddf4472bb5014b132ec331fd5e09421917d183ce31a58fa7a272b01b25d","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"f15072fedb61b6526c65f8dc0bee871bf51fe413de8bddf6a74edc0985aec41784cb54c4d756f0bc36e871a981e46ce23361345d8d092c9212ea92a995897c06"}}}],"coinoutputs":[{"value":"10000000000","condition":{"type":1,"data":{"unlockhash":"01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214"}}},{"value":"89000000000","condition":{}}],"minerfees":["1000000000"],"arbitrarydata":"ZnJvbSBtZSAoMik="}},"coininputoutputs":[{"value":"100000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["b910bb831df2454bc739f90a9854649f0f6a6be215497e14205a8e25d159d551","445579891a0c84b3b362f5266204c7b34cebe50b9d55ea6c9a05048baf7b5bf2"],"coinoutputunlockhashes":["01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214",""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"7273cb1475fe04ea9f0ba1fd3e201fc39b416a580a5d0b3b8444e2e49b75bd95","height":8766,"parent":"c7db16c052e7899b03ff2e31d1dbd176420f816199c884a5ca080a328b028965","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"d3446e886a480405f74a78bc8347f5b822abc58622fa0ef102f4f4272dede799","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"5206f05fe42b4ba41658284dab74ab7f70ef47513d4ef4e0e9a9f361df8eee16d524ffdb311593d1373fa838447c7a36434568c833ed5820224b64334fd6ab0c"}}}],"coinoutputs":[{"value":"1000000000","condition":{}},{"value":"2000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"4000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["4f524b591aea65c5b36c8ef18102f2a69d6a7e07c54e3cedbd6fc85ac8ed2611","0846ce4e40bd153f4b24c1131908ba87e2c99d78615c16eaac846cb3ca033562"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"8603ede968d434a5c61cf6cc8bf474aa6225823e72d500ad20b90293408a2694","height":11264,"parent":"ff6d7607ae89047482eb647ba915a1e305fcc5d0115686ab69d6cbf35f6b82b6","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"e2a567179c6e9fda9d30d5476a74cbc297829852afc23c644b566555a71e2a3b","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"77b026caf2cb18ccd628043e9f8728a064036d1ee845eb638b9dc44a4c7a7171e2513d2161172b574341268d7c142d78e20af978576265c1c0bd37a2327b250e"}}},{"parentid":"996d4956f5de5354a63ff644bcac26c30f3fe1f2a18ae17a457cd999bd8e9447","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"658dc60c13bd677679a904b0e7dc847b471841648679de40586aa2542a2b235c3dd3ece8e6b7b74678107d782c7608db4c6695f18ab1192a6048d1a9c423da09"}}}],"coinoutputs":[{"value":"100000000000","condition":{}},{"value":"15000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"31000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"},{"value":"85000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["ea75d01b64a05e1652bbc334a9fabf8ec0fa11f02c7d3657b4be3f3270a927d5","cf83f6453aaa7a49db8c448a86bf5e26715075a5b608e15d1628df5d2e1ed4ae"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"972482a9407b16272b6f79e7df27d1ebe29587ab76081c8569f098fc33998768","height":11264,"parent":"ff6d7607ae89047482eb647ba915a1e305fcc5d0115686ab69d6cbf35f6b82b6","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"1744c053787a5662fad3651c0ed6c68b8bb5584370a81c95aa15cfcf220bfe13","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"9085545b4884a0724925ad88e311199961a51e018f985ba262d7516a0293c416e774ead5f1de44012e784522b12cc43bc3ba1680b4df1bf25785ab2e7094c200"}}}],"coinoutputs":[{"value":"1000000000","condition":{}},{"value":"999999999","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"2999999999","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["4834fadc322aa9cfdef0294e98624424c1f972523d335f8ae45175b1035f8958","de7ce2184e2a5c6f2f0d643a1ea08902459c2ee983127051f240a6819ae4bc35"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"9e537af0eb87f6820341a7b435195ed89f0b3e003bb4c3715f30d6a713645bb7","height":7055,"parent":"fd5cfca2da14430c6e42ae65d15af9268addc469258cdb62d14553c8f05757a3","rawtransaction":{"version":129,"data":{"nonce":"IBKoTH6nDgM=","mintfulfillment":{"type":1,"data":{"publickey":"ed25519:32b9bdde2a079a4e0b75ab38b281ed67baabeff5dc27b1792190a0be900f6d90","signature":"e679cbddecb145d3d79fc4604c1ddd1443f59340e0e2f968623713b1d540615cd253a305bd456cb0f0cc125d3a2a2aa60408518927233884c53b3dba045a1e02"}},"coinoutputs":[{"value":"1000000000","condition":{}}],"minerfees":["1000000000"],"arbitrarydata":"bW9yZSBmb3IgYWxs"}},"coininputoutputs":null,"coinoutputids":["ebd166582e892cdbbc01b71c29b9a0e64f0f69eb91e7a1d99ffde99307ecaa2e"],"coinoutputunlockhashes":[""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"9fcf663997809994acf89899f029e9e1eccb4ee64390af3797f771a61ea14575","height":6805,"parent":"ef827bb13a75e61126fe75d9a6fd1956a10a5feb824259c03fe04e1dc9a57968","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"47e816e82e699e4e15c2d03d1a69d24a8c49933a4fc09f2d28d23c3fbf3b8c90","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"99904e9745db92a8ac155ac9b4a59de8fde2757269ce76ed2640f010cc9b6235774115193fc55c96cdced3997f6688ffad7a4db56a2809c41cc591b46d746b02"}}}],"coinoutputs":[{"value":"10000000000","condition":{"type":1,"data":{"unlockhash":"01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214"}}},{"value":"475999999500","condition":{}}],"minerfees":["1000000000"],"arbitrarydata":"ZnJvbSBtZSgxKQ=="}},"coininputoutputs":[{"value":"486999999500","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["d4d8124abbecf29f965dc4186bbaa4c42758202775310522e9168609e85952ad","28bcc4bdef67f304b64b4525443c5257f775ea89122a6b9f2f4526af701aaeff"],"coinoutputunlockhashes":["01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214",""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"c15ccc0e6120d156104b9b2fa64adf6688a4d6b9bfaa56b87215b5d1b92c076a","height":12165,"parent":"231f22fab108316d06bd3c33a8189560ea5e7322dfb62dcaf6f21ea437ceedfc","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"8908d1b7af0ed9d9a16c00dcbccd583c027c737df4233cd70c5c94abf6f177ff","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"bb0cef5bef645b4a8cd77986bf5923dbb54415157bb113615da71fdded9109f8e30e04264066381c3d2782f1733063076974596d9c9faf76e420fc9dcd763704"}}}],"coinoutputs":[{"value":"1000000000","condition":{"type":3,"data":{"locktime":1609412400,"condition":{}}}},{"value":"11000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"],"arbitrarydata":"aGFwcHkgZWFybHkgbmV3IHllYXI="}},"coininputoutputs":[{"value":"13000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["ed1a8a793203d59c9a43483a78fc0143f5cab3881e94c928ecc46443127ae14f","efc235db4100bc88a01bf48cb15df0ac5f3efc2aa634c563dc7b61b9c837e083"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"c1faca5dbf14484df8ea5ee9555946d34853f1af154fb2ecf45802af3fd58390","height":7011,"parent":"97e2632ca8941a04ceaf688aec591926726a5786adba5887d3372bf98c5c3bd0","rawtransaction":{"version":129,"data":{"nonce":"Q9QjsC/7ixI=","mintfulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"8e0fd7a3f710b6bece93e9fcdf0da742512bd3010f068348f242cda97f914dad3fac922f7225023d501c42e3a944910d5baa4df5b0e23f777332f86b329b3408"}},"coinoutputs":[{"value":"1000000000000000","condition":{"type":3,"data":{"locktime":42,"condition":{}}}}],"minerfees":["1000000000"],"arbitrarydata":"Y29pbnMgZm9yIGFsbCB0aGUgcGVvcGxl"}},"coininputoutputs":null,"coinoutputids":["5cc1cdcd0962403ee112509033c87eca5e07468f3c996f1f1e3240a6e806a920"],"coinoutputunlockhashes":[""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"c4c17978c29e4fbc1c202c9b46b641efad059250f0fa4009d19ff252425f7e40","height":12181,"parent":"1cae514a987b8d5d5f13ee9d22998146c75bc633078f43df3540ab8f8ad1f7a4","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"e4691377980ad92560769a1ae7161f7e4cceec065542ae72000a66fbb3154232","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"aa489200decf5b2c7b9623f0c5819d9ece8cbd8115e71b65e5965ddd10521ab28a5a12d829010d88524a46783bd04ab60de21e5d7f85f057b2290c32b06aa009"}}}],"coinoutputs":[{"value":"1000000000","condition":{}},{"value":"2000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"],"arbitrarydata":"bW9yZSBmcmVlIG1vbmV5"}},"coininputoutputs":[{"value":"4000000000","condition":{"type":3,"data":{"locktime":1262300400,"condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["126e7a270a3548a67e7756497506a4a53e578d5b818d7dec28117f92f8b74a6d","e04651829ae0e4636a958057c1426c4fc63569ccb04406b54bce472c3322af86"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"ce1b49ec09d52e18b8e9038f6fc4a51627f1a417cfc044d995cce416f06b7802","height":6827,"parent":"dbd1bc09dd3c501a8674a699c297cd1dd50bf3d0d87a2c79a80c313f85375361","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"fe236bf66b542be84d50e0445449f6eddb11ffd93aa044040a73e35a3b33d8d9","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"116602636fa757b92b1ac06837cbcfecb7e0ceb553cc07ef819b557b872cc671ec27971171ba180595fa4d35bc748d6be9e899d0802179a355c07f2d9739100e"}}}],"coinoutputs":[{"value":"10000000000","condition":{"type":1,"data":{"unlockhash":"01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214"}}},{"value":"89000000000","condition":{}}],"minerfees":["1000000000"],"arbitrarydata":"ZnJvbSBtZSAoMyk="}},"coininputoutputs":[{"value":"100000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["de63dc7d73748cb41909688a29f52e7eb32aef37c30738d1e5c993bab26c7066","5ff190d50ea0d63ecfdd1500aa146344864c82512e1492947405552e1689d31a"],"coinoutputunlockhashes":["01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214",""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"ce8f3ee3835afb7f587ab2473bf9eaacda7dbd27f8f36761ca62f9f12af68ecc","height":7026,"parent":"b38334513e11a5b93988af07b6ea8f39c808be6a3b0478f9f8a6bd7728a5f235","rawtransaction":{"version":129,"data":{"nonce":"Ewj99diiO6U=","mintfulfillment":{"type":3,"data":{"pairs":[{"publickey":"ed25519:9e310aa31e236f4f1da9c5384138674dc68323da2d8d6cf6e8ee5055b88b61e3","signature":"d39465e4522a08de394001160d0da5fd3dc4c2ca53ee6c571bf368786a66d137ace2b2ac927d09195ea32bd9e4cb6fc979e7994b8ea99b638f29408f41388207"},{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"d5bf7d9948d9125fdb15a17cf03c30405ebd4d4dbbbb3d86884edd5062d6ceddd7b0a54c1c2f5d80f4e6ca352a9a66c2642a89d1b9ae185face9af6c740bfe00"}]}},"coinoutputs":[{"value":"42000000000","condition":{}}],"minerfees":["1000000000"]}},"coininputoutputs":null,"coinoutputids":["63891de50dcb285689e1cd02618917ab9df4c6001f14e63532a5a75716ec0b6c"],"coinoutputunlockhashes":[""],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"ffd4ebd18d71c58674b28b116fc1cf67385a71b01b43104d817488dfd7e1c4c1","height":12159,"parent":"b93a31ee0eb16200101b07a4fd962bb8a8d928682b8d252a818fd7b56ff459e3","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"cf83f6453aaa7a49db8c448a86bf5e26715075a5b608e15d1628df5d2e1ed4ae","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"59cc566ac52b46eccf63480530dede3f773f289137ae3b1b333bdb09ae2d065983828af1751b28be76c31d61e445ca0e24abda60d1403b08b9edaaeab9e91402"}}}],"coinoutputs":[{"value":"1000000000","condition":{"type":3,"data":{"locktime":1549571431,"condition":{}}}},{"value":"13000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"15000000000","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["9a8f6b4524e07d7f0d2ece2a0d00c31fad9082ee21d4966af0ba9130c6f4eb6f","8908d1b7af0ed9d9a16c00dcbccd583c027c737df4233cd70c5c94abf6f177ff"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}',
    )
    explorer_client.chain_info = '{"blockid":"552e410481cce1358ffcd4687f4199dd2181c799d55da26178e55643355bbd2e","difficulty":"27801","estimatedactivebs":"59","height":3644,"maturitytimestamp":1549012510,"target":[0,2,91,116,78,165,130,72,116,162,127,4,125,67,108,16,140,247,132,198,107,159,114,177,44,25,18,162,38,157,169,245],"totalcoins":"0","arbitrarydatatotalsize":6,"minerpayoutcount":3650,"transactioncount":3652,"coininputcount":12,"coinoutputcount":15,"blockstakeinputcount":3644,"blockstakeoutputcount":3645,"minerfeecount":7,"arbitrarydatacount":1}'
    explorer_client.hash_add(
        "552e410481cce1358ffcd4687f4199dd2181c799d55da26178e55643355bbd2e",
        '{"hashtype":"blockid","block":{"minerpayoutids":["468db689f752414702ef3a5aa06238f03a4539434a61624b3b8a0fb5dc38a211"],"transactions":[{"id":"2396f8e57bbb9b22bd1d749d5de3fd532ea6886e9660a556a13571d701d83e27","height":3644,"parent":"552e410481cce1358ffcd4687f4199dd2181c799d55da26178e55643355bbd2e","rawtransaction":{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"ff5a002ec356b7cb24fbee9f076f239fb8c72d5a8a448cee92ee6d29a87aef52","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"7bec94dfb87640726c6a14de2110599db0f81cf9fa456249e7bf79b0c74b79517edde25c4ee87f181880af44fe6ee054ff20b74eda2144fe07fa5bfb9d884208"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}},"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"blockstakeoutputids":["f683e7319659c61f54e93546bc41b57c5bffe79de26c06ec7371034465804c81"],"blockstakeunlockhashes":["015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"],"unconfirmed":false}],"rawblock":{"parentid":"47db4274551b0372564f8d1ab89c596428f00e460c0b416327e53983c8765198","timestamp":1549012665,"pobsindexes":{"BlockHeight":3643,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":[{"value":"10000000000","unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"transactions":[{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"ff5a002ec356b7cb24fbee9f076f239fb8c72d5a8a448cee92ee6d29a87aef52","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"7bec94dfb87640726c6a14de2110599db0f81cf9fa456249e7bf79b0c74b79517edde25c4ee87f181880af44fe6ee054ff20b74eda2144fe07fa5bfb9d884208"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}}]},"blockid":"552e410481cce1358ffcd4687f4199dd2181c799d55da26178e55643355bbd2e","difficulty":"27801","estimatedactivebs":"59","height":3644,"maturitytimestamp":1549012510,"target":[0,2,91,116,78,165,130,72,116,162,127,4,125,67,108,16,140,247,132,198,107,159,114,177,44,25,18,162,38,157,169,245],"totalcoins":"0","arbitrarydatatotalsize":6,"minerpayoutcount":3650,"transactioncount":3652,"coininputcount":12,"coinoutputcount":15,"blockstakeinputcount":3644,"blockstakeoutputcount":3645,"minerfeecount":7,"arbitrarydatacount":1},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":null,"multisigaddresses":null,"unconfirmed":false}',
    )
    c._explorer_get = explorer_client.explorer_get

    # you can also get the balance from an unlock hash results
    balance = c.unlockhash_get(
        "000000000000000000000000000000000000000000000000000000000000000000000000000000"
    ).balance()
    assert len(balance.outputs_spent) == 0
    assert str(balance.available) == "1000843.999999501"
    assert str(balance.locked) == "2"

    # a balance can be drained,
    # meaning all confirmed outputs are spent
    txns = balance.drain(
        recipient="01ffd7c884aa869056bfb832d957bb71a0005fee13c19046cebec84b3a5047ee8829eab070374b",
        miner_fee=c.minimum_miner_fee,
        data="drain the swamp",
        lock="06/06/2018 06:58",
    )
    assert len(txns) == 1
    txn = txns[0]
    # the given miner fee is used as the only miner fee
    assert len(txn.miner_fees) == 1
    assert txn.miner_fees[0] == c.minimum_miner_fee
    # the data should be asigned
    assert txn.data.value == b"drain the swamp"
    # all inputs should be orinating from the balance's available outputs
    assert [ci.parentid for ci in txn.coin_inputs] == [co.id for co in balance.outputs_available]
    assert len(txn.coin_outputs) == 1
    # the only output should be the drain output
    co = txn.coin_outputs[0]
    assert co.condition.unlockhash == "01ffd7c884aa869056bfb832d957bb71a0005fee13c19046cebec84b3a5047ee8829eab070374b"
    assert co.value == (balance.available - c.minimum_miner_fee)
    # no block stake inputs or outputs are obviously defined
    assert len(txn.blockstake_inputs) == 0
    assert len(txn.blockstake_outputs) == 0

    # NOTE: balance.drain also takes an optional parameter 'unconfirmed` which is False by default,
    # if True unconfirmed outputs will also be used when available.

    c.delete()
