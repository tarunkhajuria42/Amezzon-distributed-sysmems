from viewmodel.GenericViewModel import GenericViewModel


class LoginViewModel(GenericViewModel):
    def __init__(self, username=None, password=None, error_message=None, error=False):
        GenericViewModel.__init__(self, error_message)
        self.username = username
        self.password = password
        self.error = error

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def isError(self):
        return self.error

    def set_error(self, error):
        self.error = error
