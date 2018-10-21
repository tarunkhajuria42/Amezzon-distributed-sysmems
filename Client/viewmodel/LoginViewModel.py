from viewmodel.GenericViewModel import GenericViewModel


class LoginViewModel(GenericViewModel):
    def __init__(self, user_name=None, password=None, error_message=None):
        GenericViewModel.__init__(self, error_message)
        self.username = user_name
        self.password = password

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
