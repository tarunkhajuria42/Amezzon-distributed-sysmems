from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from resource.StaticResource import LOGIN_SCREEN
from service.RegistrationScreenService import RegistrationService
from viewmodel.RegistrationViewModel import RegistrationViewModel

Builder.load_file("view/RegistrationScreen.kv")


class RegistrationScreen(Screen):
    def __init__(self, **kw):
        super(RegistrationScreen, self).__init__(**kw)
        self.connectionManager = ObjectProperty(None)

        self.first_name = ObjectProperty(None)
        self.last_name = ObjectProperty(None)
        self.email = ObjectProperty(None)
        self.username = ObjectProperty(None)
        self.password = ObjectProperty(None)
        self.confirm_password = ObjectProperty(None)
        self.error_message = ObjectProperty(None)

        self.registrationService = RegistrationService()
        self.registrationViewModel = RegistrationViewModel()
        self.bind_trigger = Clock.create_trigger(self.bind_model)

    def on_enter(self, *args):
        if self.registrationViewModel.get_username() is None:
            self.bind_trigger()

    def on_leave(self, *args):
        self.reset_model()

    def bind_model(self, *args):
        self.registrationViewModel.set_first_name(first_name=self.first_name)
        self.registrationViewModel.set_last_name(last_name=self.last_name)
        self.registrationViewModel.set_email(email=self.email)
        self.registrationViewModel.set_username(username=self.username)
        self.registrationViewModel.set_password(password=self.password)
        self.registrationViewModel.set_confirm_password(confirm_password=self.confirm_password)
        self.registrationViewModel.set_error_message(error_message=self.error_message)

    def reset_model(self):
        self.registrationViewModel.get_first_name().text = ''
        self.registrationViewModel.get_last_name().text = ''
        self.registrationViewModel.get_email().text = ''
        self.registrationViewModel.get_username().text = ''
        self.registrationViewModel.get_password().text = ''
        self.registrationViewModel.get_confirm_password().text = ''
        self.registrationViewModel.get_error_message().text = ''

    def to_login_screen(self):
        self.parent.transition.direction = 'right'
        self.parent.current = LOGIN_SCREEN

    def registration(self):
        self.registrationService.register(
            registrationViewModel=self.registrationViewModel,
            connectionManager=self.connectionManager,
            registrationScreen=self)
