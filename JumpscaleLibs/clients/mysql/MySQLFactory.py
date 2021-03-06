from Jumpscale import j
from .MySQLClient import MySQLClient
import time
import calendar

try:
    import mysql.connector
except:
    j.builders.runtimes.python3.pip_package_install("mysql-connector")
    import mysql.connector

JSConfigs = j.baseclasses.object_config_collection


class MySQLFactory(JSConfigs):
    """
    """

    __jslocation__ = "j.clients.mysql"
    _CHILDCLASS = MySQLClient

    def _init(self, **kwargs):
        self.clients = {}

    def get(self, name=None, id=None, die=True, create_new=True, childclass_name=None, **kwargs):
        return self.getClient(name=name, id=id, die=die, create_new=create_new, **kwargs)

    def getClient(self, name=None, id=None, die=True, create_new=True, **kwargs):
        cl = JSConfigs.get(self, name=name, id=id, die=die, create_new=create_new, **kwargs)

        key = "%s_%s_%s_%s_%s" % (cl.ipaddr, cl.port, cl.login, cl.passwd, cl.dbname)
        if key not in self.clients:
            self.clients[key] = mysql.connector.connect(
                host=cl.ipaddr, user=cl.login, password=cl.passwd, database=cl.dbname, port=cl.port
            )
        cl.client = self.clients[key]
        return cl
