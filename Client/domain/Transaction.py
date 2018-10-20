from domain.GenericModel import GenericModel
from domain.Person import Person
from domain.TransactionType import TransactionType


class Transaction(GenericModel):
    def __init__(self, id=None, transaction_type=TransactionType(), person=Person(), price=None,
                 quantity=None, date_time=None):
        self.id = id
        self.transaction_type = transaction_type
        self.person = person
        self.price = price
        self.quantity = quantity
        self.date_time = date_time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_transaction_type(self):
        return self.transaction_type

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def get_person(self):
        return self.person

    def set_person(self, person):
        self.person = person

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_date_time(self):
        return self.date_time

    def set_date_time(self, date_time):
        self.date_time = date_time