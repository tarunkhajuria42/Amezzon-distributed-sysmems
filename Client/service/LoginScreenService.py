import httplib
import socket
from dto.LoginDto import LoginDto
from resource.StaticResource import HOME_SCREEN


class LoginService(object):
    def __init__(self):
        self.loginDto = LoginDto()
        self.loginViewModel = None
        self.loginScreen = None

    def validate_input(self):
        if (self.loginViewModel.get_username().text and
                self.loginViewModel.get_password().text):
            return True
        else:
            if not self.loginViewModel.get_username().text:
                self.loginViewModel.get_username().focus = True

            if not self.loginViewModel.get_password().text:
                self.loginViewModel.get_password().focus = True

            return False

    # TODO:Validate return value before moving to Home Screen
    def login(self, loginViewModel, connectionManager, loginScreen):
        self.loginScreen = loginScreen
        self.loginViewModel = loginViewModel

        if self.validate_input():
            self.loginScreen.transition.direction = 'down'
            self.loginScreen.current = HOME_SCREEN
        #     requestDto = self.loginDto.PostRequest(
        #         username=self.loginViewModel.get_username().text,
        #         password=self.loginViewModel.get_password().text
        #     )
        #     try:
        #         response = connectionManager.send_request(body=requestDto.toJSON(), method='POST')
        #         self.loginScreen.current = REGISTRATION_SCREEN
        #     except (httplib.HTTPException, socket.error) as ex:
        #         print "Error: %s" % ex
