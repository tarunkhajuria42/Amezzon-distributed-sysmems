from domain.Product import Product
from dto.ErrorMessage import ErrorMessageList
from dto.GenericDto import GenericDto
from resource.StaticResource import ACTION_PRODUCTS


class ProductDto(object):
    class GetRequest(GenericDto.CustomAuthRequest):
        def __init__(self, token=None):
            GenericDto.CustomAuthRequest.__init__(
                self, action=ACTION_PRODUCTS, token=token,
                data=self.Data()
            )

        class Data(object):
            def __init__(self):
                pass

    class GetResponse(GenericDto.CustomResponse):
        def __init__(self, error_messages=None, product_list=None, response_date_time=None):
            GenericDto.CustomResponse.__init__(
                self, data=self.Data(
                    error_messages=error_messages,
                    product_list=product_list,
                    response_date_time=response_date_time
                )
            )

        class Data(object):
            def __init__(self, error_messages, product_list, response_date_time):
                if error_messages is None:
                    error_messages = []
                if product_list is None:
                    product_list = []
                self.error_messages = error_messages
                self.product_list = product_list
                self.response_date_time = response_date_time

            def get_error_messages(self):
                return self.error_messages

            def set_error_messages(self, error_messages):
                self.error_messages = error_messages

            def add_error(self, message):
                self.error_messages.append(message)

            def get_product_list(self):
                return self.product_list

            def set_product_list(self, product_list):
                self.product_list = product_list

            def add_product(self, product):
                self.product_list.append(product)
