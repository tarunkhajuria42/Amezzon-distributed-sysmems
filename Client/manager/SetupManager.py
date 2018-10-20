TEMP_FOLDERS = "temp_folders"


class SetupManager(object):
    def __init__(self, service_manager):
        self.folder_service = service_manager.get_folder_service()
        self.folder_config = service_manager.get_folder_config()
        self.log_service = service_manager.get_log_service()

    def folder_setup(self):
        folder_dict = dict(self.folder_config._sections)[TEMP_FOLDERS]
        for label in folder_dict:
            if not self.folder_service.folder_exists(folder_dict[label]):
                self.folder_service.create_folder(folder_dict[label])

    def log_setup(self):
        self.log_service.set_logger()

    def run_setup(self):
        self.folder_setup()
        self.log_setup()
