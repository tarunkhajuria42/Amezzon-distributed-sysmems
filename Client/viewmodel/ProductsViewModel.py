class ProductsViewModel(object):
    def __init__(self, product_list=None):
        if product_list is None:
            product_list = []
        self.product_list = product_list

    def get_product_list(self):
        return self.product_list

    def set_product_list(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)