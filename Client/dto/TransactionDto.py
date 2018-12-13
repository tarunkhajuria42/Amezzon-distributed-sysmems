from dto.GenericDto import GenericDto
from resource.StaticResource import ACTION_TRANSACTION


class TransactionDto(object):
    class GetRequest(GenericDto.CustomAuthRequest):
        def __init__(self, token=None, action=None, product_id=None,
                     buy_price=None, sell_price=None, product_quantity=None):
            GenericDto.CustomAuthRequest.__init__(
                self, action=ACTION_TRANSACTION, token=token,
                data=self.Data(action=action, product_id=product_id, buy_price=buy_price,
                               sell_price=sell_price, product_quantity=product_quantity)
            )

        class Data(object):
            def __init__(self, action, product_id, buy_price, sell_price, product_quantity):
                self.action = action
                self.product_id = product_id
                self.buy_price = buy_price
                self.sell_price = sell_price
                self.product_quantity = product_quantity

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
                pass
