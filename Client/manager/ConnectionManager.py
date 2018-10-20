from httplib import HTTPSConnection

CONNECTION_DEFAULT = 'default'
PORT = 'port'
HOST = 'host'


class ConnectionManager(object):
    def __init__(self, service_manager):
        self.connection_config = service_manager.get_connection_config()
        self.connection_service = service_manager.get_connection_service()
        self.connection = None

    def set_connection(self):
        conf = dict(self.connection_config._sections)[CONNECTION_DEFAULT]
        self.connection = HTTPSConnection("{0}:{1}".format(conf[HOST], conf[PORT]))
        self.connection.request('GET', '')
        print self.connection.getresponse()