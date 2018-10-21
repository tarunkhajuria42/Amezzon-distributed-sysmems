from domain.GenericModel import GenericModel
from domain.Product import Product


class Pile(GenericModel):
    def __init__(self, id=None, product=Product(), amount=None):
        self.id = id
        self.product = product
        self.amount = amount

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
