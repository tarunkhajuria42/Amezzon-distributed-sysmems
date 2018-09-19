from configparser import SafeConfigParser
from services.FolderService import FolderService


class SetupManager:
    __folder_service = FolderService()

    def __init__(self):
        self.conf_file = "conf.ini"
        self.temp_folders = "temp_folders"

        self.parser = SafeConfigParser()
        self.parser.read(self.conf_file)

        self.folder_setup()

    def folder_setup(self):
        folder_dict = dict(self.parser._sections)[self.temp_folders]
        for label in folder_dict:
            if not self.__folder_service.folder_exists(folder_dict[label]):
                self.__folder_service.creat_folder(folder_dict[label])