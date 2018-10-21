from dto.ErrorMessage import ErrorMessages
from dto.GenericDto import GenericDto


class UserInformationDto(object):
    class GetRequest(GenericDto.CustomAuthRequest):
        def __init__(self, action=None, token=None, data=None):
            GenericDto.CustomAuthRequest.__init__(
                self, action=action, token=token, data=data)

        class Data(object):
            def __init__(self):
                pass

    class GetResponse(GenericDto.CustomResponse):
        def __init__(self, first_name=None, last_name=None, mail=None,
                     username=None, id_number=None, error_messages=None):
            GenericDto.CustomResponse.__init__(
                self, data=self.Data(
                    first_name=first_name, last_name=last_name, mail=mail,
                    username=username, id_number=id_number, error_messages=error_messages
                )
            )

        class Data(ErrorMessages):
            def __init__(self, first_name=None, last_name=None, mail=None,
                         username=None, id_number=None, error_messages=None):
                ErrorMessages.__init__(self, error_messages=error_messages)
                self.first_name = first_name
                self.last_name = last_name
                self.mail = mail
                self.username = username
                self.id_number = id_number

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

            def set_mail(self, mail):
                self.mail = mail

            def get_id_number(self):
                return self.id_number

            def set_id_number(self, id_number):
                self.id_number = id_number

    class PostRequest(GenericDto.CustomAuthRequest):
        def __init__(self, action=None, token=None, first_name=None,
                     last_name=None, mail=None, password=None):
            GenericDto.CustomAuthRequest.__init__(
                self, action=action, token=token, data=self.Data(
                    first_name=first_name, last_name=last_name,
                    mail=mail, password=password
                )
            )

        class Data(object):
            def __init__(self, first_name=None, last_name=None,
                         mail=None, password=None):
                self.first_name = first_name
                self.last_name = last_name
                self.mail = mail
                self.password = password

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

            def set_mail(self, mail):
                self.mail = mail

            def get_password(self):
                return self.password

            def set_password(self, password):
                self.password = password

    class PostResponse(GenericDto.CustomResponse):
        def __init__(self, error_messages=None):
            GenericDto.CustomResponse.__init__(
                self, data=self.Data(error_messages=error_messages)
            )

        class Data(ErrorMessages):
            def __init__(self, error_messages=None):
                ErrorMessages.__init__(self, error_messages=error_messages)
