from kivy.app import App
from dto.LoginDto import LoginDto
from handler.ScreenManager import ScreenManager
from manager.SetupManager import SetupManager
from manager.ServiceManager import ServiceManager
from manager.ConnectionManager import ConnectionManager


def run():
    service_manager = ServiceManager()
    SetupManager(service_manager=service_manager).run_setup()
    connection_manager = ConnectionManager(service_manager=service_manager)


class MainApp(App):
    def build(self):
        return ScreenManager()


if __name__ == '__main__':
    MainApp().run()
