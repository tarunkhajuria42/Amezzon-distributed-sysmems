from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

# NB !!!!!!!! DO NOT REMOVE !!!!!!!!!!
from handler.LoginScreen import LoginScreen
from handler.HomeScreen import HomeScreen
from handler.RegistrationScreen import RegistrationScreen

Builder.load_file("view/MainScreenManager.kv")


class MainScreenManager(ScreenManager):
    token = None

    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        self.loginScreen = ObjectProperty(None)
        self.registrationScreen = ObjectProperty(None)
        self.homeScreen = ObjectProperty(None)
        self.token = None
