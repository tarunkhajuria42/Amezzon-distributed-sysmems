from viewmodel.GenericViewModel import GenericViewModel


class LoginViewModel(GenericViewModel):
    def __init__(self,
                 username=None, username_error_message=None,
                 password=None, password_error_message=None,
                 error_message=None, error=False):
        GenericViewModel.__init__(self, error_message)

        self.username = username
        self.username_error_message = username_error_message

        self.password = password
        self.password_error_message = password_error_message

        self.error = error

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_username_error_message(self):
        return self.username_error_message

    def set_username_error_message(self, username_error_message):
        self.username_error_message = username_error_message

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_password_error_message(self):
        return self.password_error_message

    def set_password_error_message(self, password_error_message):
        self.password_error_message = password_error_message

    def isError(self):
        return self.error

    def set_error(self, error):
        self.error = error
