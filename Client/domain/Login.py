from domain.GenericModel import GenericModel


class Login(GenericModel):
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
