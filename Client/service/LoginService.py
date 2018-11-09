import httplib
import socket
import urllib, json
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

    def login(self, loginViewModel, connection_manager):
        self.loginViewModel = loginViewModel
        if self.validate_input():
            reqDto = self.loginDto.PostRequest(
                username=self.loginViewModel.get_username().text,
                password=self.loginViewModel.get_password().text
            )
            try:
                res = connection_manager.send_request(body=reqDto.toJSON(), method='POST')
                print res
            except (httplib.HTTPException, socket.error) as ex:
                print "Error: %s" % ex
