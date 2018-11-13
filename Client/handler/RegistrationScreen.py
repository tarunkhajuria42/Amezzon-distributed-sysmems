from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/RegistrationScreen.kv")

LOGIN_SCREEN = 'LoginScreen'


class RegistrationScreen(Screen):
    def __init__(self, **kw):
        super(RegistrationScreen, self).__init__(**kw)

    def to_login_screen(self):
        self.parent.current = LOGIN_SCREEN
