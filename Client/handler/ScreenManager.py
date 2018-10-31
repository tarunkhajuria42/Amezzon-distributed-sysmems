from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
import LoginScreen
import RegistrationScreen


Builder.load_file("view/ScreenManager.kv")


class ScreenManager(ScreenManager):
    login_screen = ObjectProperty(None)
    registration_screen = ObjectProperty(None)
