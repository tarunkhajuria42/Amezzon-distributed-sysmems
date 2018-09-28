from services.FolderService import FolderService
from services.LogService import LogService


class ServiceManager(object):
    def __init__(self):
        self._folder_service = FolderService()
        self._log_service = LogService()

    @property
    def folder_service(self):
        return self._folder_service

    @folder_service.getter
    def folder_service(self):
        return self._folder_service

    @property
    def log_service(self):
        return self._log_service

    @log_service.getter
    def log_service(self):
        return self._log_service
