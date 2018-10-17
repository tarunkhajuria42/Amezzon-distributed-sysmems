from domain.ProductType import ProductType


class Product(object):
    def __init__(self, id=None, name=None, description=None, product_type=ProductType()):
        self._id = id
        self._name = name
        self._description = description
        self._product_type = product_type

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
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.getter
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def product_type(self):
        return self._product_type

    @product_type.getter
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, type_id):
        self._product_type = type_id
