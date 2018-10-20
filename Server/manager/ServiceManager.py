from configparser import SafeConfigParser
from service.FolderService import FolderService
from service.LogService import LogService

FOLDER_CONF_FILE = 'conf/folder_config.ini'
LOG_CONF_FILE = 'conf/logging_config.ini'
SERVER_CONF_FILE = 'conf/server_config.ini'


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

        """SetUp log related service and configurations"""
        self.server_config = SafeConfigParser()
        self.server_config.read(SERVER_CONF_FILE)

    def get_folder_service(self):
        return self.folder_service

    def get_folder_config(self):
        return self.folder_config

    def get_log_service(self):
        return self.log_service

    def get_log_config(self):
        return self.log_config

    def get_server_config(self):
        return self.server_config
