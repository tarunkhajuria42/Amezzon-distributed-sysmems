class Login(object):

    def __init__(self, user_name=None, password=None):
        self._user_name = user_name
        self._password = password

    @property
    def user_name(self):
        return self._user_name

    @user_name.getter
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @user_name.deleter
    def user_name(self):
        del self._user_name

    @property
    def password(self):
        return self._password

    @password.getter
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @password.deleter
    def password(self):
        del self._password

    def __eq__(self, other):
        return (self._password == other._password and
                self._user_name == other._user_name)
