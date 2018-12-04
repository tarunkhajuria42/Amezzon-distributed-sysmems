from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from resource.StaticResource import REGISTRATION_SCREEN

Builder.load_file("view/PersonalInformationScreen.kv")


class PersonalInformationScreen(Screen):
    def __init__(self, **kwargs):
        super(PersonalInformationScreen, self).__init__(**kwargs)
