from dto.client.ErrorMessage import ErrorMessages
from dto.client.GenericDto import GenericDto
from resource.DtoResource import ACTION_REGISTRATION


class RegistrationDto(object):
    class PostRequest(GenericDto.CustomRequest):
        def __init__(self, login=False, username=None, password=None,
                     first_name=None, last_name=None, mail=None, id_code=None):
            GenericDto.CustomRequest.__init__(
                self, action=ACTION_REGISTRATION, data=self.Data(
                    username=username, password=password,
                    first_name=first_name, last_name=last_name,
                    mail=mail, id_code=id_code)
            )
            self.login = login

        def isLogin(self):
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

            def get_first_name(self):
                return self.first_name

            def set_first_name(self, first_name):
                self.first_name = first_name

            def get_last_name(self):
                return self.last_name

            def set_last_name(self, last_name):
                self.last_name = last_name

            def get_mail(self):
                return self.mail

            def set_mail(self, email):
                self.mail = email

            def get_id_code(self):
                return self.id_code

            def set_id_code(self, id_code):
                self.id_code = id_code

            def get_username(self):
                return self.username

            def set_username(self, username):
                self.username = username

            def get_password(self):
                return self.password

            def set_password(self, password):
                self.password = password

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