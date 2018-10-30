from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from viewmodel.LoginViewModel import LoginViewModel

Builder.load_file("view/LoginScreen.kv")

REGISTRATION_SCREEN = 'RegistrationScreen'


class LoginScreen(Screen):
    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        self.loginViewModel = LoginViewModel()
        self.username = ObjectProperty(None)
        self.password = ObjectProperty(None)

    def bind_view_model(self):
        self.loginViewModel.set_username(self.username)
        self.loginViewModel.set_password(self.password)

    def to_registration_screen(self):
        self.parent.current = REGISTRATION_SCREEN

    def login(self):
        self.bind_view_model()
        print self.loginViewModel.get_username().text
