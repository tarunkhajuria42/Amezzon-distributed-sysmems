import os
import ssl
from manager.ServerThreadManager import ServerThreadManager
from resource.StaticResource import SERVER_CONFIG
from service.HttpHandlerService import HttpHandlerService

CRL_PATH = 'crl/yourpemfile.pem'


class ConnectionManager(object):
    def __init__(self, service_manager):
        self.service_manager = service_manager
        self.server_config = dict(service_manager.get_server_config()._sections)[SERVER_CONFIG]
        self.server = ServerThreadManager(
            (
                self.server_config['host'],
                int(self.server_config['port'])
            ),
            HttpHandlerService
        )
        # self.server.socket = ssl.wrap_socket(
        #     sock=self.server.socket,
        #     server_side=self.server_config['server_side'],
        #     certfile=CRL_PATH
        # )

    def run(self):
        print 'Starting server, Accepting Clients'
        print' Server running at :'+ str(self.server_config['host'])+':'+ str(self.server_config['port'])
        self.server.serve_forever()
