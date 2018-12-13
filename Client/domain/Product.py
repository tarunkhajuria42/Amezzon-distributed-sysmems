from domain.GenericModel import GenericModel
from domain.ProductType import ProductType


class Product(GenericModel):
    def __init__(self, id=None, name=None, description=None, buy=None,
                 sell=None, quantity=None, product_type=ProductType()):
        self.id = id
        self.name = name
        self.description = description
        self.product_type = product_type
        self.buy = buy
        self.sell = sell
        self.quantity = quantity

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_buy(self):
        return self.buy

    def set_buy(self, buy):
        self.buy = buy

    def get_sell(self):
        return self.sell

    def set_sell(self, sell):
        self.sell = sell

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_product_type(self):
        return self.product_type

    def set_product_type(self, product_type):
        self.product_type = product_type
