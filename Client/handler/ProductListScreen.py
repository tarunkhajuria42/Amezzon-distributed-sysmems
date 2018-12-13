from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from resource.StaticResource import PRODUCT_SCREEN
from service.ProductListScreenService import ProductListScreenService
from viewmodel.ProductListViewModel import ProductListViewModel

Builder.load_file("view/ProductListScreen.kv")


class ProductListScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductListScreen, self).__init__(**kwargs)
        self.connectionManager = ObjectProperty(None)
        self.productListViewModel = ProductListViewModel()
        self.productListScreenService = ProductListScreenService()
        self.spinner = ObjectProperty(None)
        self.bind_trigger = Clock.create_trigger(self.bind_model)
        self.event = None

    def callback(self, *args):
        self.productListScreenService.set_list_data()

    def on_enter(self, *args):
        self.bind_trigger()
        self.event = Clock.schedule_interval(self.callback, 5)

    def on_leave(self, *args):
        self.productListScreenService.hide_list()
        self.event.cancel()

    def on_product_select(self, *args):
        listItem = args[0]
        self.parent.ids.productScreen.id = listItem.id
        self.parent.current = PRODUCT_SCREEN

    def bind_model(self, *args):
        if self.parent.token is not None:
            if self.productListScreenService.spinner is None:
                self.productListScreenService.bind_objects(productListScreen=self)

            self.productListScreenService.set_list_data()
