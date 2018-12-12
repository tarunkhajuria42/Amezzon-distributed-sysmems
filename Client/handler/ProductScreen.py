import thread
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from service.ProductScreenService import ProductScreenService

Builder.load_file("view/ProductScreen.kv")


class ProductScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)
        self.connectionManager = ObjectProperty(None)
        self.productScreenService = ProductScreenService()

        self.id = None
        self.product_name = ObjectProperty(None)
        self.description = ObjectProperty(None)
        self.buy_price = ObjectProperty(None)
        self.sell_price = ObjectProperty(None)
        self.current_quantity = ObjectProperty(None)
        self.input_quantity = ObjectProperty(None)

        self.spinner = ObjectProperty(None)
        self.scrollView = ObjectProperty(None)

        self.bind_trigger = Clock.create_trigger(self.bind_model)

    def on_enter(self, *args):
        self.bind_trigger()

    def on_leave(self, *args):
        self.productScreenService.hide_product()

    def buy(self):
        print 'buy'

    def sell(self):
        print 'sell'

    def bind_model(self, *args):
        self.productScreenService.bind_objects(productScreen=self)
        thread.start_new_thread(self.productScreenService.update_product, ())
