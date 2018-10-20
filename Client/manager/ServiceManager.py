from service.FolderService import FolderService
from service.LogService import LogService


class ServiceManager(object):
    def __init__(self):
        self.folder_service = FolderService()
        self.log_service = LogService()

    def get_folder_service(self):
        return self.folder_service

    def get_log_service(self):
        return self.log_service
