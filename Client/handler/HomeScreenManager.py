from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

# NB !!!!!!!!!!!!!! DO NOT REMOVE !!!!!!!!
from handler.AppInformationScreen import AppInformationScreen
from handler.PersonalInformationScreen import PersonalInformationScreen
from handler.ProductListScreen import ProductListScreen
from handler.TransactionHistoryScreen import TransactionHistoryScreen

Builder.load_file("view/HomeScreenManager.kv")


class HomeScreenManager(ScreenManager):
    token = None

    def __init__(self, **kwargs):
        super(HomeScreenManager, self).__init__(**kwargs)
        self.productsScreen = ObjectProperty(None)
        self.transactionHistoryScreen = ObjectProperty(None)
        self.personalInformationScreen = ObjectProperty(None)
        self.appInformationScreen = ObjectProperty(None)
