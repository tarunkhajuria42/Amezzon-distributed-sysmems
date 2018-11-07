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
                self.loginViewModel.get_username_error_message().height = 50
                self.loginViewModel.get_username_error_message().text = 'Please provide a Username'

            if not self.loginViewModel.get_password().text:
                self.loginViewModel.get_password_error_message().height = 50
                self.loginViewModel.get_password_error_message().text = 'Please provide a Password'
            return False

    def login(self, loginViewModel):
        self.loginViewModel = loginViewModel
        if self.validate_input():
            print 'OK'
            # reqDto = self.loginDto.PostRequest(username=username, password=password)
            # res = self.connection_manager.send_request(body=reqDto.toJSON(), method='POST')
