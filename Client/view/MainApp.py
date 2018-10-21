from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    pass


class RegistrationScreen(Screen):
    pass


class MainScreen(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return presentation
