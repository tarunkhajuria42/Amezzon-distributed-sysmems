from configparser import SafeConfigParser

CONF_FILE = "conf.ini"
TEMP_FOLDERS = "temp_folders"


class SetupManager(object):
    def __init__(self, service_manager):
        self.parser = SafeConfigParser()
        self.parser.read(CONF_FILE)

        self.__folder_service = service_manager.get_folder_service()
        self.__log_service = service_manager.get_log_service()

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
