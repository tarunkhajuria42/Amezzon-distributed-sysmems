from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from service.LoginService import LoginService
from viewmodel.LoginViewModel import LoginViewModel

Builder.load_file("view/LoginScreen.kv")

REGISTRATION_SCREEN = 'RegistrationScreen'


class LoginScreen(Screen):
    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        self.login_service = LoginService()
        self.connection_manager = ObjectProperty(None)
        self.username = ObjectProperty(None)
        self.password = ObjectProperty(None)
        self.username_error_message = ObjectProperty(None)
        self.password_error_message = ObjectProperty(None)
        self.loginViewModel = LoginViewModel()

    def bind_view_model(self):
        self.loginViewModel.set_username(self.username)
        self.loginViewModel.set_username_error_message(self.username_error_message)

        self.loginViewModel.set_password(self.password)
        self.loginViewModel.set_password_error_message(self.password_error_message)

    def to_registration_screen(self):
        self.parent.current = REGISTRATION_SCREEN

    def on_username_change(self, text):
        if text:
            self.username_error_message.height = 0
            self.username_error_message.text = ''

    def on_password_change(self, text):
        if text:
            self.password_error_message.height = 0
            self.password_error_message.text = ''

    def login(self):
        self.bind_view_model()
        self.login_service.login(self.loginViewModel, self.connection_manager)
