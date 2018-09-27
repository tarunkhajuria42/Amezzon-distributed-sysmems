from configparser import SafeConfigParser

CONF_FILE = "conf.ini"
TEMP_FOLDERS = "temp_folders"


class SetupManager(object):
    def __init__(self, service_manager):
        self.parser = SafeConfigParser()
        self.parser.read(CONF_FILE)

        self._folder_service = service_manager.folder_service
        self._log_service = service_manager.log_service

    def folder_setup(self):
        folder_dict = dict(self.parser._sections)[TEMP_FOLDERS]
        for label in folder_dict:
            if not self._folder_service.folder_exists(folder_dict[label]):
                self._folder_service.create_folder(folder_dict[label])

    def log_setup(self):
        self._log_service.set_logger()

    def run_setup(self):
        self.folder_setup()
        self.log_setup()
