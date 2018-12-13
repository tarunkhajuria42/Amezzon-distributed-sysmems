import httplib
import socket

from pandas import json

from dto.ProductDto import ProductDto
from dto.TransactionDto import TransactionDto


class ProductScreenService(object):
    def __init__(self):
        self.connectionManager = None
        self.productScreen = None

        self.spinner = None
        self.scrollView = None

    def bind_objects(self, productScreen):
        self.productScreen = productScreen
        self.connectionManager = productScreen.connectionManager
        self.spinner = productScreen.spinner
        self.scrollView = productScreen.scrollView

    def update_product(self):
        requestDto = ProductDto().GetRequest(
            token=self.productScreen.parent.token,
            product_id=int(self.productScreen.id))
        try:
            response = json.loads(self.connectionManager.send_request(
                body=requestDto.toJSON(),
                method='GET'))['data']['product_list'][0]
            self.productScreen.product_name.text = response['product_name']
            self.productScreen.product_description.text = response['product_description']
            self.productScreen.buy_price.text = 'Buy price: {0}'.format(
                format(float(response['buy_price']), '.3f')
            )
            self.productScreen.sell_price.text = 'Sell price: {0}'.format(
                format(float(response['sell_price']), '.3f')
            )
            self.productScreen.current_quantity.text = 'Quantity: {0}'.format(
                int(response['product_quantity'])
            )
            self.show_product()
        except (httplib.HTTPException, socket.error) as ex:
            print 'products request error {0}'.format(ex)

    def product_buy(self):
        self.hide_product()
        self.product_action(action="BUY")

    def product_sell(self):
        self.hide_product()
        self.product_action(action="SELL")

    def product_action(self, action):
        requestDto = TransactionDto().GetRequest(
            token=self.productScreen.parent.token,
            action=action,
            product_id=int(self.productScreen.id),
            buy_price=self.productScreen.buy_price.text.split(":")[1],
            sell_price=self.productScreen.sell_price.text.split(":")[1],
            product_quantity=self.productScreen.input_quantity.text)
        try:
            response = json.loads(self.connectionManager.send_request(body=requestDto.toJSON(), method='GET'))
            self.validate_response(response=response)
            self.show_product()
        except (httplib.HTTPException, socket.error) as ex:
            print 'products request error {0}'.format(ex)

    def validate_response(self, response):
        if response['data']['error_messages'][0]['message'] is None:
            self.productScreen.buy_price.text = 'Buy price: {0}'.format(
                format(float(response['data']['buy_price']), '.3f')
            )
            self.productScreen.sell_price.text = 'Sell price: {0}'.format(
                format(float(response['data']['sell_price']), '.3f')
            )
            self.productScreen.current_quantity.text = 'Quantity: {0}'.format(
                int(response['data']['quantity'])
            )
        else:
            print 'error'

    def validate_input(self):
        if not self.productScreen.input_quantity.text:
            self.productScreen.input_quantity.focus = True
            return False
        else:
            try:
                int(self.productScreen.input_quantity.text)
                return True
            except ValueError:
                self.productScreen.input_quantity.focus = True
                return False

    def show_product(self):
        self.scrollView.opacity = 1
        self.spinner.opacity = 0
        self.spinner.active = False

    def hide_product(self):
        self.scrollView.opacity = 0
        self.spinner.opacity = 1
        self.spinner.active = True
