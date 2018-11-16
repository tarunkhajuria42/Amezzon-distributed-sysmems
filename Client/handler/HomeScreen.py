from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from service.HomeScreenService import HomeScreenService
from viewmodel.HomeViewModel import HomeViewModel

Builder.load_file("view/HomeScreen.kv")


class HomeScreen(Screen):
    def __init__(self, **kw):
        super(HomeScreen, self).__init__(**kw)
        self.connectionManager = ObjectProperty(None)

        self.homeViewModel = HomeViewModel()
        self.homeScreenService = HomeScreenService()
