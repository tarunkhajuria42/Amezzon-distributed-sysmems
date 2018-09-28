from domain.GenericO import GenericO
from domain.Product import Product


class Pile(GenericO):
    def __init__(self, id=None, product=Product(), amount=None):
        self._id = id
        self._product = product
        self._amount = amount

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
    def product(self):
        return self._product

    @product.getter
    def product(self):
        return self._product

    @product.setter
    def product(self, product=Product()):
        self._product = product

    @property
    def amount(self):
        return self._amount

    @amount.getter
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
