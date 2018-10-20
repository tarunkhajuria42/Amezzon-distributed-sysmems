from manager.SetupManager import SetupManager
from manager.ServiceManager import ServiceManager


def run():
    service_manager = ServiceManager()
    set_up_manager = SetupManager(service_manager)
    set_up_manager.run_setup()


if __name__ == '__main__':
    run()