from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, SlideTransition, NoTransition

from kivy.properties import ObjectProperty
from kivymd.navigationdrawer import NavigationLayout, MDNavigationDrawer

# NB !!!!!! DO NOT REMOVE !!!!!
from handler.HomeScreenManager import HomeScreenManager
from resource.StaticResource import LOGIN_SCREEN

Builder.load_file("view/HomeScreen.kv")


class HomeScreen(Screen):
    token = None

    def __init__(self, **kw):
        super(HomeScreen, self).__init__(**kw)
        self.connectionManager = ObjectProperty(None)
        self.homeScreenManager = ObjectProperty(None)
        self.navigationLayout = NavigationLayout()
        self.mdNavigationDrawer = MDNavigationDrawer()
        self.bind_trigger = Clock.create_trigger(self.bind_model)

    def on_enter(self, *args):
        if self.parent.token is not None:
            self.bind_trigger()

    def bind_model(self, *args):
        self.token = self.parent.token
        self.homeScreenManager.token = self.token
        self.homeScreenManager.transition = NoTransition()
        self.homeScreenManager.current = 'LoadingScreen'
        self.homeScreenManager.current = 'ProductListScreen'
        self.homeScreenManager.transition = SlideTransition()
        self.homeScreenManager.transition.direction = 'left'

    def leave(self):
        self.parent.token = None
        self.parent.transition.direction = 'up'
        self.parent.current = LOGIN_SCREEN
