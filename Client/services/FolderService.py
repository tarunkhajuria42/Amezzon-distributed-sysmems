import platform
import os


class FolderService:

    def __init__(self):
        self.windows = "Windows"
        self.linux = "Linux"
        self.apple = "Apple"
        self.system_os = platform.system()
        self.root_path = os.getcwd()

    def remove_folder(self, path):
        print path

    def creat_folder(self, path):
        os.makedirs(self.root_path + path)

    def folder_exists(self, path):
        return os.path.exists(self.root_path + path)
