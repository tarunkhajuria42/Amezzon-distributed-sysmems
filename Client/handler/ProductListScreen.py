from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.list import TwoLineListItem, MDList

from domain.Product import Product
from service.ProductService import ProductService
from viewmodel.ProductListViewModel import ProductListViewModel

Builder.load_file("view/ProductListScreen.kv")


class ProductListScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductListScreen, self).__init__(**kwargs)
        self.connectionManager = ObjectProperty(None)
        self.productListViewModel = ProductListViewModel()
        self.productService = ProductService()
        self.scrollView = None
        self.bind_trigger = Clock.create_trigger(self.bind_model)
        self.stamp = None

        self.set_mock_data()

    def on_enter(self, *args):
        self.bind_trigger()

    def on_product_select(self, *args):
        item = args[0]
        print item.id

    def bind_model(self, *args):
        if self.parent.token is not None and self.scrollView is None:
            self.bind_list()

    def bind_list(self):
        self.scrollView = ScrollView()
        self.add_widget(self.scrollView)

        mdList = MDList()
        self.scrollView.add_widget(mdList)

        # self.productListViewModel.set_product_list()

        for product in self.productListViewModel.get_product_list():
            item = TwoLineListItem(
                id=product.id,
                text=product.name,
                secondary_text='Buy price:{0}\n Sell price:{1}'.format(product.buy, product.sell),
                on_release=self.on_product_select
            )
            mdList.add_widget(item)

    def set_mock_data(self):
        for i in range(10):
            self.productListViewModel.add_product(
                product=Product(
                    id='{0}'.format(i), name='Test {0}'.format(i), description='dhaiuhdwiud waiuhdiusahdiuwa dhiuah diwahddhwa iuda',
                    buy=(1 + i) * 100.00, sell=(1 + i) * 100.00
                )
            )
