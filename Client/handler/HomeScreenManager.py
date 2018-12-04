from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from handler.AppInformationScreen import AppInformationScreen
from handler.PersonalInformationScreen import PersonalInformationScreen
from handler.ProductsScreen import ProductsScreen
from handler.TransactionHistoryScreen import TransactionHistoryScreen

Builder.load_file("view/HomeScreenManager.kv")


class HomeScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(HomeScreenManager, self).__init__(**kwargs)
        self.productsScreen = ProductsScreen()
        self.transactionHistoryScreen = TransactionHistoryScreen()
        self.personalInformationScreen = PersonalInformationScreen()
        self.appInformationScreen = AppInformationScreen()
