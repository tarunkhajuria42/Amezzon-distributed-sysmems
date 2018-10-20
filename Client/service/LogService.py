import platform
import logging
import os
from logging.config import fileConfig

LOG_CONFIG_FILE = 'conf/logging_config.ini'
LOG_FILE = 'client.log'
LOG_NAME = 'sLogger'


class LogService(object):

    def __init__(self):
        self._logger = None
        self.system_os = platform.system()
        self.root_path = os.getcwd()

    def log_file_exists(self):
        return os.path.exists(self.root_path + LOG_FILE)

    def set_logger(self):
        fileConfig(self.root_path + LOG_CONFIG_FILE)
        self._logger = logging.getLogger(LOG_NAME)

    def log_event(self, message):
        self._logger.debug(message)
