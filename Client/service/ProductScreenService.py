import httplib
import socket

from pandas import json

from dto.ProductDto import ProductDto


class ProductScreenService(object):
    def __init__(self):
        self.connectionManager = None
        self.productScreen = None

        self.spinner = None
        self.scrollView = None

    def bind_objects(self, productScreen):
        self.productScreen = productScreen
        self.spinner = productScreen.spinner
        self.scrollView = productScreen.scrollView

    def update_product(self):
        self.hide_product()
        requestDto = ProductDto().GetRequest(
            token=self.productScreen.parent.token,
            product_id=int(self.productScreen.id))
        try:
            response = json.loads(self.connectionManager.send_request(body=requestDto.toJSON(), method='GET'))
            print response
        except (httplib.HTTPException, socket.error) as ex:
            print 'products request error {0}'.format(ex)

    def show_product(self):
        self.scrollView.opacity = 1
        self.spinner.opacity = 0
        self.spinner.active = False

    def hide_product(self):
        self.scrollView.opacity = 0
        self.spinner.opacity = 1
        self.spinner.active = True
