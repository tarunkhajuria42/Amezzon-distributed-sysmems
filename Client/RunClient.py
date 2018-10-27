from dto.LoginDto import LoginDto
from manager.SetupManager import SetupManager
from manager.ServiceManager import ServiceManager
from manager.ConnectionManager import ConnectionManager


def run():
    service_manager = ServiceManager()
    SetupManager(service_manager=service_manager).run_setup()
    connection_manager = ConnectionManager(service_manager=service_manager)

    dto = LoginDto.PostRequest(
        username='Aleksei',
        password='TEST'
    )
    body = dto.toJSON()
    response = connection_manager.send_request(body=body, method='POST')
    print response.read()


if __name__ == '__main__':
    run()