from configparser import SafeConfigParser
from services.FolderService import FolderService
from services.LogService import LogService

FOLDER_CONF_FILE = 'conf/folder_config.ini'
LOG_CONF_FILE = 'conf/logging_config.ini'
SERVER_CONF_FILE = 'conf/server_config.ini'


class ServiceManager(object):
    def __init__(self):
        """SetUp folder related services and configurations"""
        self._folder_config = SafeConfigParser()
        self.folder_config.read(FOLDER_CONF_FILE)
        self._folder_service = FolderService()

        """SetUp log related services and configurations"""
        self._log_config = SafeConfigParser()
        self.log_config.read(LOG_CONF_FILE)
        self._log_service = LogService()


        """SetUp log related services and configurations"""
        self._server_config = SafeConfigParser()
        self.server_config.read(SERVER_CONF_FILE)

    @property
    def folder_service(self):
        return self._folder_service

    @folder_service.getter
    def folder_service(self):
        return self._folder_service

    @property
    def folder_config(self):
        return self._folder_config

    @folder_config.getter
    def folder_config(self):
        return self._folder_config

    @property
    def log_service(self):
        return self._log_service

    @log_service.getter
    def log_service(self):
        return self._log_service

    @property
    def log_config(self):
        return self._log_config

    @log_config.getter
    def log_config(self):
        return self._log_config

    @property
    def server_config(self):
        return self._server_config

    @server_config.getter
    def server_config(self):
        return self._server_config
