from managers.SetupManager import SetupManager
from managers.ServiceManager import ServiceManager
from managers.ServerManager import ServerManager


def run():
    service_manager = ServiceManager()

    set_up_manager = SetupManager(service_manager=service_manager)
    set_up_manager.run_setup()

    # todo: wait for setup manager to finish all functions then run
    server = ServerManager(service_manager=service_manager)
    server.run()


if __name__ == '__main__':
    run()
