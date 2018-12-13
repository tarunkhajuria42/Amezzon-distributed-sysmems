from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from resource.StaticResource import REGISTRATION_SCREEN
from service.LoginScreenService import LoginService
from viewmodel.LoginViewModel import LoginViewModel

Builder.load_file("view/AppInformationScreen.kv")


class AppInformationScreen(Screen):
    def __init__(self, **kwargs):
        super(AppInformationScreen, self).__init__(**kwargs)
