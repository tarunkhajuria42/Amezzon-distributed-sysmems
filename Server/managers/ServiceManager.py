from services.FolderService import FolderService
from services.LogService import LogService


class ServiceManager(object):

    def __init__(self):
        self.__folder_service = FolderService()
        self.__log_service = LogService()

    def get_folder_service(self):
        return self.__folder_service

    def get_log_service(self):
        return self.__log_service
