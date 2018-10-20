from domain.GenericModel import GenericModel


class Person(GenericModel):
    def __init__(self, id=None, first_name=None, last_name=None, email=None, id_number=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id_number = id_number

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_id_number(self):
        return self.id_number

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)
