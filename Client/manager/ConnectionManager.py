import httplib
import ssl

CRL_PATH = 'crl/yourpemfile.pem'
CONNECTION_DEFAULT = 'default'
PORT = 'port'
HOST = 'host'


class ConnectionManager(object):
    def __init__(self, service_manager):
        self.con_config = dict(service_manager.get_connection_config())[CONNECTION_DEFAULT]
        self.con_service = service_manager.get_connection_service()
        self.connection = None

    def set_connection(self):
        url = "{0}:{1}".format(self.con_config[HOST], self.con_config[PORT])
        self.connection = httplib.HTTPConnection(url)
        self.connection.request('GET', '/')
        print self.connection.getresponse()