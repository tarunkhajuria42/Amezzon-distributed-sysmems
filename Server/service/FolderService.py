import platform
import os


class FolderService(object):

    def __init__(self):
        self.system_os = platform.system()
        self.root_path = os.getcwd()

    # Todo: remove folders
    def remove_folder(self, path):
        pass

    def create_folder(self, path):
        os.makedirs(self.root_path + path)

    def folder_exists(self, path):
        return os.path.exists(self.root_path + path)
