import httplib
import socket
import thread
import json

from kivy.uix.scrollview import ScrollView
from kivymd.list import MDList, TwoLineListItem

from domain.Product import Product
from dto.ProductDto import ProductDto


class ProductListScreenService(object):
    def __init__(self):
        self.connectionManager = None
        self.productListScreen = None
        self.productListViewModel = None

        self.scrollView = None
        self.mdList = None
        self.spinner = None

    def bind_objects(self, productListScreen):
        self.productListScreen = productListScreen
        self.connectionManager = productListScreen.connectionManager
        self.productListViewModel = productListScreen.productListViewModel
        self.spinner = productListScreen.spinner

        self.scrollView = ScrollView()
        self.productListScreen.add_widget(widget=self.scrollView)

        self.mdList = MDList()
        self.scrollView.add_widget(widget=self.mdList)

    def set_mdList(self):
        if len(self.mdList.children) is 0:
            for product in self.productListViewModel.get_product_list():
                print product.id
                print product.name
                print product.buy
                print product.sell
                item = TwoLineListItem(
                    id=str(product.id),
                    text=str(product.name),
                    secondary_text='Buy price:{0} Sell price:{1}'.format(str(product.buy), str(product.sell)),
                    on_release=self.productListScreen.on_product_select
                )
                self.mdList.add_widget(item)
        else:
            for i in range(len(self.mdList.children)):
                self.mdList.children[i].id = self.productListViewModel.get_product_list()[i].id
                self.mdList.children[i].text = self.productListViewModel.get_product_list()[i].name
                self.mdList.children[i].secondary_text = 'Buy price:{0} Sell price:{1}'.format(
                    self.productListViewModel.get_product_list()[i].buy,
                    self.productListViewModel.get_product_list()[i].sell)

        self.mdList.opacity = 1
        self.spinner.opacity = 0
        self.spinner.active = False

    def send_request(self):
        requestDto = ProductDto.GetRequest(token=self.productListScreen.parent.token)

        try:
            response = json.loads(self.connectionManager.send_request(body=requestDto.toJSON(), method='GET'))
            # response = json.loads(self.mock_response())
            product_list = response['data']['product_list']
            temp_list = []
            for product_json in product_list:
                product = Product(
                    id=product_json['product_id'],
                    name=product_json['product_name'],
                    description=product_json['product_description'],
                    buy=product_json['buy_price'],
                    sell=product_json['sell_price'],
                    quantity=product_json['product_quantity'],
                    product_type=product_json['type']
                )
                temp_list.append(product)
            self.productListViewModel.set_product_list(product_list=temp_list)
            self.set_mdList()
        except (httplib.HTTPException, socket.error) as ex:
            print 'products request error {0}'.format(ex)

    def set_list_data(self):
        self.mdList.opacity = 0
        self.spinner.opacity = 1
        self.spinner.active = True
        thread.start_new_thread(self.send_request, ())

    def mock_response(self):
        response = ProductDto.GetResponse()
        for i in range(4):
            p = {
                'product_id': '{0}'.format(i),
                'product_name': 'test {0}'.format(i),
                'product_description': 'djaiodjwaoidjsiajd',
                'buy_price': (1 + i) * 100.00,
                'sell_price': (1 + i) * 100.00,
                'product_quantity': (1 + i) * 100.00,
                'product_type': 'type {0}'.format(i)
            }
            response.get_data().add_product(product=p)
        return response.toJSON()
