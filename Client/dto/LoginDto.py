from dto.ErrorMessage import ErrorMessages
from dto.GenericDto import GenericDto


class LoginDto(object):
    class PostRequest(GenericDto.CustomRequest):
        def __init__(self, action=None, username=None, password=None):
            GenericDto.CustomRequest.__init__(
                self, action=action, data=self.Data(username=username, password=password)
            )

        class Data(object):
            def __init__(self, username=None, password=None):
                self.username = username
                self.password = password

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
