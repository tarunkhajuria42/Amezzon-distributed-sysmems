import httplib
import socket
from dto.LoginDto import LoginDto


class LoginService(object):
    def __init__(self):
        self.loginDto = LoginDto()
        self.loginViewModel = None

    def validate_input(self):
        if self.loginViewModel.get_username().text and self.loginViewModel.get_password().text:
            return True
        else:
            if not self.loginViewModel.get_username().text:
                self.loginViewModel.get_username().hint_text = 'Login'

            if not self.loginViewModel.get_password().text:
                self.loginViewModel.get_password().hint_text = 'Password'

            return False

    def login(self, loginViewModel, connectionManager):
        self.loginViewModel = loginViewModel
        if self.validate_input():
            requestDto = self.loginDto.PostRequest(
                username=self.loginViewModel.get_username().text,
                password=self.loginViewModel.get_password().text
            )
            try:
                response = connectionManager.send_request(body=requestDto.toJSON(), method='POST')
                print response
            except (httplib.HTTPException, socket.error) as ex:
                print "Error: %s" % ex
