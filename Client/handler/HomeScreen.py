from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.properties import ObjectProperty
from kivymd.navigationdrawer import NavigationLayout, MDNavigationDrawer

from handler.HomeScreenManager import HomeScreenManager
from resource.StaticResource import LOGIN_SCREEN

Builder.load_file("view/HomeScreen.kv")


class HomeScreen(Screen):
    def __init__(self, **kw):
        super(HomeScreen, self).__init__(**kw)
        self.connectionManager = ObjectProperty(None)
        self.token = None

        self.navigationLayout = NavigationLayout()
        self.mdNavigationDrawer = MDNavigationDrawer()
        self.homeScreenManager = HomeScreenManager()

        self.bind_trigger = Clock.create_trigger(self.bind_model)

    def on_enter(self, *args):
        self.bind_trigger()

    def bind_model(self, *args):
        self.token = self.parent.token

    def leave(self):
        self.token = None
        self.parent.token = None
        self.parent.transition.direction = 'up'
        self.parent.current = LOGIN_SCREEN
