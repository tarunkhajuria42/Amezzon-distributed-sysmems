from manager.SetupManager import SetupManager
from manager.ServiceManager import ServiceManager
from manager.ConnectionManager import ConnectionManager


def run():
    service_manager = ServiceManager()
    SetupManager(service_manager=service_manager).run_setup()
    ConnectionManager(service_manager=service_manager).run()


if __name__ == '__main__':
    run()
