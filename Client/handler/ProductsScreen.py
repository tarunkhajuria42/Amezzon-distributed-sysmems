from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from resource.StaticResource import REGISTRATION_SCREEN
from viewmodel.ProductsViewModel import ProductsViewModel

Builder.load_file("view/ProductsScreen.kv")


class ProductsScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductsScreen, self).__init__(**kwargs)
        self.productsViewModel = ProductsViewModel()
