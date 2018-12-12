from configparser import SafeConfigParser

from service.ConnectionService import ConnectionService
from service.FolderService import FolderService
from service.LogService import LogService


FOLDER_CONF_FILE = 'conf/folder_config.ini'
LOG_CONF_FILE = 'conf/logging_config.ini'
CLIENT_CONF_FILE = 'conf/client_config.ini'


class ServiceManager(object):
    def __init__(self):
        """SetUp folder related service and configurations"""
        self.folder_config = SafeConfigParser()
        self.folder_config.read(FOLDER_CONF_FILE)
        self.folder_service = FolderService()

        """SetUp log related service and configurations"""
        self.log_config = SafeConfigParser()
        self.log_config.read(LOG_CONF_FILE)
        self.log_service = LogService()

        """Connection service"""
        self.connection_config = SafeConfigParser()
        self.connection_config.read(CLIENT_CONF_FILE)
        self.connection_service = ConnectionService()

    def get_folder_service(self):
        return self.folder_service

    def get_folder_config(self):
        return self.folder_config

    def get_log_service(self):
        return self.log_service

    def get_log_config(self):
        return self.log_config

    def get_connection_config(self):
        return self.connection_config

    def get_connection_service(self):
        return self.connection_service
