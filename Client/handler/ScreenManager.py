from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from handler.LoginScreen import LoginScreen
from handler.RegistrationScreen import RegistrationScreen

Builder.load_file("view/ScreenManager.kv")


class ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManager, self).__init__(**kwargs)
        self.login_screen = LoginScreen()
        self.registration_screen = RegistrationScreen()
