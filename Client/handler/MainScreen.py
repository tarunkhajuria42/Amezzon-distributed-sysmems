from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from handler.LoginScreen import LoginScreen
from handler.HomeScreen import HomeScreen
from handler.RegistrationScreen import RegistrationScreen

Builder.load_file("view/MainScreen.kv")


class MainScreen(ScreenManager):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)
        self.loginScreen = LoginScreen()
        self.registrationScreen = RegistrationScreen()
        self.homeScreen = HomeScreen()
