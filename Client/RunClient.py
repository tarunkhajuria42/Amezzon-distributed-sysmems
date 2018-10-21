from manager.SetupManager import SetupManager
from manager.ServiceManager import ServiceManager
from manager.ConnectionManager import ConnectionManager


def run():
    service_manager = ServiceManager()
    setup_manager = SetupManager(service_manager=service_manager)
    setup_manager.run_setup()
    connection_manager = ConnectionManager(service_manager=service_manager)
    connection_manager.set_connection()


if __name__ == '__main__':
    run()