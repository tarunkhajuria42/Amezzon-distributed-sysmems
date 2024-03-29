from kivy.app import App

from kivymd.theming import ThemeManager

from handler.MainScreenManager import MainScreenManager
from manager.ConnectionManager import ConnectionManager
from manager.ServiceManager import ServiceManager
from manager.SetupManager import SetupManager
from kivy.config import Config


class MainApp(App):
    connectionManager = None
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Blue"
    Config.set('graphics', 'width', '590')
    Config.set('graphics', 'height', '600')
    Config.write()

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.service_manager = ServiceManager()
        SetupManager(service_manager=self.service_manager).run_setup()
        self.connectionManager = ConnectionManager(service_manager=self.service_manager)
        self.mainScreenManager = MainScreenManager()

    def build(self):
        return self.mainScreenManager


if __name__ == '__main__':
    app = MainApp()
    app.run()
