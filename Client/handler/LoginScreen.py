from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from resource.StaticResource import REGISTRATION_SCREEN
from service.LoginScreenService import LoginService
from viewmodel.LoginViewModel import LoginViewModel

Builder.load_file("view/LoginScreen.kv")


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.connectionManager = ObjectProperty(None)

        self.username = ObjectProperty(None)
        self.password = ObjectProperty(None)
        self.error_message = ObjectProperty(None)

        self.loginService = LoginService()
        self.loginViewModel = LoginViewModel()
        self.bind_trigger = Clock.create_trigger(self.bind_model)

    def on_enter(self, *args):
        if self.loginViewModel.get_username() is None:
            self.bind_trigger()

    def bind_model(self, *args):
        self.loginViewModel.set_username(username=self.username)
        self.loginViewModel.set_password(password=self.password)
        self.loginViewModel.set_error_message(error_message=self.error_message)

    def on_leave(self, *args):
        self.reset_model()

    def reset_model(self):
        self.loginViewModel.get_error_message().text = ''
        self.loginViewModel.get_username().text = ''
        self.loginViewModel.get_password().text = ''

    def to_registration_screen(self):
        self.parent.transition.direction = 'left'
        self.parent.current = REGISTRATION_SCREEN

    def login(self):
        self.loginService.login(
            loginViewModel=self.loginViewModel,
            connectionManager=self.connectionManager,
            loginScreen=self)
