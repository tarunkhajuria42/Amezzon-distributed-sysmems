from kivy.app import App
from handler.ScreenManager import ScreenManager
from manager.ConnectionManager import ConnectionManager
from manager.ServiceManager import ServiceManager
from manager.SetupManager import SetupManager


class MainApp(App):
    connection_manager = None

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.service_manager = ServiceManager()
        SetupManager(service_manager=self.service_manager).run_setup()
        self.connection_manager = ConnectionManager(service_manager=self.service_manager)

    def build(self):
        return ScreenManager()


if __name__ == '__main__':
    app = MainApp()
    app.run()
