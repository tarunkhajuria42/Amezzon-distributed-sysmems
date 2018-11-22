import httplib
import socket

from dto.RegistrationDto import RegistrationDto


class RegistrationService(object):
    def __init__(self):
        self.registrationDto = RegistrationDto()
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

    def register(self, registrationViewModel, connectionManager, registrationScreen):
        self.registrationScreen = registrationScreen
        self.registrationViewModel = registrationViewModel

        if self.validate_input():
            requestDto = self.registrationDto.PostRequest(
                first_name=self.registrationViewModel.get_first_name().text,
                last_name=self.registrationViewModel.get_last_name().text,
                username=self.registrationViewModel.get_username().text,
                password=self.registrationViewModel.get_password().text,
                mail=self.registrationViewModel.get_email().text
            )
            try:
                response = connectionManager.send_request(body=requestDto.toJSON(), method='POST')
                print response
            except (httplib.HTTPException, socket.error) as ex:
                print "Error: %s" % ex
