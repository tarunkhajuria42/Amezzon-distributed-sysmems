import ssl
from managers.ServerThreadManager import ServerThreadManager
from services.HttpHandlerService import HttpHandlerService

SERVER_CONFIG = 'default'
CRL_PATH = 'crl/yourpemfile.pem'


class ServerManager:
    def __init__(self, service_manager):
        self._service_manager = service_manager
        self._server_config = dict(service_manager.server_config._sections)[SERVER_CONFIG]
        self._server = ServerThreadManager(
            (
                self._server_config['host'],
                int(self._server_config['port'])
            ),
            HttpHandlerService
        )
        self._server.socket = ssl.wrap_socket(
            sock=self._server.socket,
            server_side=self._server_config['server_side'],
            certfile=CRL_PATH
        )

    def run(self):
        print 'Starting server, Accepting Clients'
        self._server.serve_forever()
