from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from resource.StaticResource import REGISTRATION_SCREEN
from service.LoginScreenService import LoginService
from viewmodel.LoginViewModel import LoginViewModel

Builder.load_file("view/LoginScreen.kv")


class LoginScreen(Screen):
    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        self.connectionManager = ObjectProperty(None)

        self.username = ObjectProperty(None)
        self.password = ObjectProperty(None)

        self.loginService = LoginService()
        self.loginViewModel = LoginViewModel()

    def bind_view_model(self):
        self.loginViewModel.set_username(username=self.username)
        self.loginViewModel.set_password(password=self.password)

    def to_registration_screen(self):
        self.parent.transition.direction = 'left'
        self.parent.current = REGISTRATION_SCREEN

    # TODO:Validate return value before moving to Home Screen
    def login(self):
        self.bind_view_model()
        self.loginService.login(
            loginViewModel=self.loginViewModel,
            connectionManager=self.connectionManager,
            loginScreen=self.parent
        )
