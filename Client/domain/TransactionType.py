from domain.GenericModel import GenericModel


class TransactionType(GenericModel):
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
