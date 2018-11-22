from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty
from kivymd.navigationdrawer import NavigationLayout, MDNavigationDrawer

from resource.StaticResource import LOGIN_SCREEN

Builder.load_file("view/HomeScreen.kv")


class HomeScreen(Screen):
    def __init__(self, **kw):
        super(HomeScreen, self).__init__(**kw)
        self.connectionManager = ObjectProperty(None)
        self.navigationLayout = NavigationLayout()
        self.mdNavigationDrawer = MDNavigationDrawer()

    def leave(self):
        self.parent.transition.direction = 'up'
        self.parent.current = LOGIN_SCREEN
