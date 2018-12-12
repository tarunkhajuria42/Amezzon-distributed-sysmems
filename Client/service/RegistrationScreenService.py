import httplib
import json
import socket
import thread

from dto.ErrorMessage import ErrorMessageList
from dto.RegistrationDto import RegistrationDto
from resource.StaticResource import HOME_SCREEN


class RegistrationService(object):
    def __init__(self):
        self.registrationDto = RegistrationDto()
        self.connectionManager = None
        self.registrationViewModel = None
        self.registrationScreen = None

    def validate_input(self):
        if (self.registrationViewModel.get_first_name().text and
                self.registrationViewModel.get_last_name().text and
                self.registrationViewModel.get_username().text and
                self.registrationViewModel.get_password().text and
                self.registrationViewModel.get_confirm_password().text and
                self.registrationViewModel.get_email().text and
                self.registrationViewModel.get_password().text ==
                self.registrationViewModel.get_confirm_password().text):
            return True
        else:
            if not self.registrationViewModel.get_first_name().text:
                self.registrationViewModel.get_first_name().focus = True

            if not self.registrationViewModel.get_last_name().text:
                self.registrationViewModel.get_last_name().focus = True

            if not self.registrationViewModel.get_username().text:
                self.registrationViewModel.get_username().focus = True

            if not self.registrationViewModel.get_password().text:
                self.registrationViewModel.get_password().focus = True

            if not self.registrationViewModel.get_confirm_password().text:
                self.registrationViewModel.get_confirm_password().helper_text = 'This field is required'
                self.registrationViewModel.get_confirm_password().focus = True

            if not self.registrationViewModel.get_email().text:
                self.registrationViewModel.get_email().focus = True

            if not (self.registrationViewModel.get_password().text ==
                    self.registrationViewModel.get_confirm_password().text):
                self.registrationViewModel.get_confirm_password().helper_text = \
                    'Password and confirm password must match'
                self.registrationViewModel.get_confirm_password().focus = True
                self.registrationViewModel.get_confirm_password().error = True
        return False

    def validate_response(self, response):
        response_json = json.loads(response)
        token = response_json['data']['token']
        error_messages_list = ErrorMessageList()
        for error in response_json['data']['error_messages']:
            error_messages_list.add_error_message(
                message=error['message'],
                message_connection=error['message_connection']
            )

        if token is not None:
            self.registrationScreen.parent.token = token
            self.registrationScreen.parent.transition.direction = 'down'
            self.registrationScreen.parent.current = HOME_SCREEN
        else:
            error_messages = error_messages_list.get_error_messages()[0]
            self.registrationViewModel.get_error_message().text = "{0}: {1}".format(
                error_messages.get_type(), error_messages.get_message())

    def send_request(self):
        requestDto = self.registrationDto.PostRequest(
            first_name=self.registrationViewModel.get_first_name().text,
            last_name=self.registrationViewModel.get_last_name().text,
            username=self.registrationViewModel.get_username().text,
            password=self.registrationViewModel.get_password().text,
            mail=self.registrationViewModel.get_email().text,
            id_code='',
            login=True)
        try:
            response = self.connectionManager.send_request(body=requestDto.toJSON(), method='POST')
            print response
            self.validate_response(response=response)
        except (httplib.HTTPException, socket.error) as ex:
            self.registrationViewModel.get_error_message().text = 'Can not connect to server'

    def register(self, registrationViewModel, connectionManager, registrationScreen):
        self.registrationScreen = registrationScreen
        self.registrationViewModel = registrationViewModel
        self.connectionManager = connectionManager

        if self.validate_input():
            thread.start_new_thread(self.send_request, ())

    # Mock data
    def mock_data_ok(self):
        return self.registrationDto.PostResponse(
            token='47681534984',
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

        return self.registrationDto.PostResponse(
            token=None,
            error_messages=messages.get_error_messages()
        ).toJSON()