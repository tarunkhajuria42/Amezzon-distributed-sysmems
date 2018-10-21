from GenericDto import GenericDto
from dto.ErrorMessage import ErrorMessages


class RegistrationDto(object):
    class PostRequest(GenericDto.CustomRequest):
        def __init__(self, action=None, login=False, username=None, password=None,
                     first_name=None, last_name=None, mail=None, id_code=None):
            GenericDto.CustomRequest.__init__(
                self, action=action, data=self.Data(
                    username=username, password=password,
                    first_name=first_name, last_name=last_name,
                    mail=mail, id_code=id_code)
            )
            self.login = login

        def get_login(self):
            return self.login

        def set_login(self, login):
            self.login = login

        class Data(object):
            def __init__(self, username=None, password=None, first_name=None,
                         last_name=None, mail=None, id_code=None):
                self.username = username
                self.password = password
                self.first_name = first_name
                self.last_name = last_name
                self.mail = mail
                self.id_code = id_code

    class PostResponse(GenericDto.CustomResponse):
        def __init__(self, token=None, error_messages=None):
            GenericDto.CustomResponse.__init__(
                self, data=self.Data(
                    error_messages=error_messages
                ))
            self.token = token

        def get_token(self):
            return self.token

        def set_token(self, token):
            self.token = token

        class Data(ErrorMessages):
            def __init__(self, error_messages=None):
                ErrorMessages.__init__(self, error_messages=error_messages)