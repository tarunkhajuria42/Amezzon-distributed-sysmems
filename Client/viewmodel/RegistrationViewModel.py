from viewmodel.GenericViewModel import GenericViewModel


class RegistrationViewModel(GenericViewModel):
    def __init__(self, error_message=None, first_name=None, last_name=None, username=None,
                 password=None, confirm_password=None, email=None, id_code=None):
        GenericViewModel.__init__(self, error_message)

        self.first_name = first_name
        self.last_name = last_name

        self.username = username
        self.password = password
        self.confirm_password = confirm_password

        self.email = email
        self.id_code = id_code

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_confirm_password(self):
        return self.confirm_password

    def set_confirm_password(self, confirm_password):
        self.confirm_password = confirm_password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_id_code(self):
        return self.id_code

    def set_id_code(self, id_code):
        self.id_code = id_code

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)