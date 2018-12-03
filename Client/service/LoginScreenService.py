import thread
import httplib
import socket
import json

from dto.ErrorMessage import ErrorMessageList
from dto.LoginDto import LoginDto
from resource.StaticResource import HOME_SCREEN


class LoginService(object):
    def __init__(self):
        self.loginDto = LoginDto()
        self.connectionManager = None
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

    def validate_response(self, response):
        response_json = json.loads(response)
        token = response_json['token']
        error_messages = response_json['data']['error_messages']
        if len(error_messages) == 0:
            self.loginScreen.parent.token = token
            self.loginScreen.parent.transition.direction = 'down'
            self.loginScreen.parent.current = HOME_SCREEN
        else:
            self.loginViewModel.get_error_message().text = 'Invalid credentials'

    def avoid_validation(self):
        self.loginScreen.parent.transition.direction = 'down'
        self.loginScreen.parent.current = HOME_SCREEN

    def send_request(self):
        requestDto = self.loginDto.PostRequest(
            username=self.loginViewModel.get_username().text,
            password=self.loginViewModel.get_password().text)
        try:
            # response = self.connectionManager.send_request(body=requestDto.toJSON(), method='POST')
            response = self.mock_data_ok()
            self.validate_response(response=response)
        except (httplib.HTTPException, socket.error) as ex:
            self.loginViewModel.get_error_message().text = 'Can not connect to server'

    def login(self, loginViewModel, connectionManager, loginScreen):
        self.loginScreen = loginScreen
        self.loginViewModel = loginViewModel
        self.connectionManager = connectionManager

        if self.validate_input():
            thread.start_new_thread(self.send_request, ())

    # Mock data
    def mock_data_ok(self):
        return self.loginDto.PostResponse(
            token='154562356456',
            error_messages=None
        ).toJSON()

    def mock_data_error(self):
        messages = ErrorMessageList()

        messages.add_error_message(
            message='Invalid credentials',
            message_connection='Login'
        )

        messages.add_error_message(
            message='Invalid credentials',
            message_connection='Login'
        )

        return self.loginDto.PostResponse(
            token=None,
            error_messages=messages.get_error_messages()
        ).toJSON()
