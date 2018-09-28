from domain.GenericO import GenericO
from domain.Person import Person
from domain.TransactionType import TransactionType


class Transaction(GenericO):
    def __init__(self, id=None, transaction_type=TransactionType(), person=Person(), price=None, quantity=None,
                 date_time=None):
        self._id = id
        self._transaction_type = transaction_type
        self._person = person
        self._price = price
        self._quantity = quantity
        self._date_time = date_time

    @property
    def id(self):
        return self._id

    @id.getter
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.getter
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type=TransactionType()):
        self._transaction_type = transaction_type
