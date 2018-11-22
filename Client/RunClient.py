from kivy.app import App

from kivymd.theming import ThemeManager

from handler.MainScreen import MainScreen
from manager.ConnectionManager import ConnectionManager
from manager.ServiceManager import ServiceManager
from manager.SetupManager import SetupManager


class MainApp(App):
    connectionManager = None
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Blue"

    def __init__(self, **kw):
        super(MainApp, self).__init__(**kw)
        self.service_manager = ServiceManager()
        SetupManager(service_manager=self.service_manager).run_setup()
        self.connectionManager = ConnectionManager(service_manager=self.service_manager)
        self.mainScreen = MainScreen()

    def build(self):
        return self.mainScreen


if __name__ == '__main__':
    app = MainApp()
    app.run()
