import httplib
import socket
import thread
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, SlideTransition, NoTransition

from kivy.properties import ObjectProperty
from kivymd.navigationdrawer import NavigationLayout, MDNavigationDrawer

# NB !!!!!! DO NOT REMOVE !!!!!
from dto.LogoutDto import LogoutDto
from handler.HomeScreenManager import HomeScreenManager
from resource.StaticResource import LOGIN_SCREEN, LOADING_SCREEN, PRODUCT_LIST_SCREEN

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
        self.homeScreenManager.current = LOADING_SCREEN
        self.homeScreenManager.current = PRODUCT_LIST_SCREEN
        self.homeScreenManager.transition = SlideTransition()
        self.homeScreenManager.transition.direction = 'left'

    def leave(self):
        thread.start_new_thread(self.logout, ())
        self.parent.token = None
        self.parent.transition.direction = 'up'
        self.parent.current = LOGIN_SCREEN
        self.homeScreenManager.current = LOADING_SCREEN

    def logout(self):
        logoutDto = LogoutDto().GetRequest(token=self.token)
        try:
            self.connectionManager.send_request(body=logoutDto.toJSON(), method='POST')
        except (httplib.HTTPException, socket.error) as ex:
            pass
