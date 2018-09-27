from configparser import SafeConfigParser
from services.FolderService import FolderService
from services.LogService import LogService

CONF_FILE = "conf.ini"
TEMP_FOLDERS = "temp_folders"


class SetupManager(object):
    __folder_service = FolderService()
    __log_service = LogService()

    def __init__(self):
        self.parser = SafeConfigParser()
        self.parser.read(CONF_FILE)

    def folder_setup(self):
        folder_dict = dict(self.parser._sections)[TEMP_FOLDERS]
        for label in folder_dict:
            if not self.__folder_service.folder_exists(folder_dict[label]):
                self.__folder_service.create_folder(folder_dict[label])

    def log_setup(self):
        self.__log_service.set_logger()

    def run_setup(self):
        self.folder_setup()
        self.log_setup()