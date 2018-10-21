from manager.SetupManager import SetupManager
from manager.ServiceManager import ServiceManager
from manager.ConnectionManager import ConnectionManager


def run():
    service_manager = ServiceManager()

    set_up_manager = SetupManager(service_manager=service_manager)
    set_up_manager.run_setup()

    # todo: wait for setup manager to finish all functions then run
    server = ConnectionManager(service_manager=service_manager)
    server.run()


if __name__ == '__main__':
    run()
