import json

from parser.client.UserInformationDtoParser import UserInformationDtoParser
from parser.client.LoginDtoParser import LoginDtoParserService
from parser.client.RegistrationDtoParser import RegistrationDtoParserService
from resource.StaticResource import ACTION_LOGIN, ACTION_REGISTRATION, \
    ACTION_USER_INFORMATION, ACTION


class ClientRequestParser(object):
    def __init__(self, json_string, method):
        self.json = json.loads(json_string)
        self.action = self.json[ACTION]
        self.method = method
        self.class_map = {
            ACTION_LOGIN: LoginDtoParserService,
            ACTION_REGISTRATION: RegistrationDtoParserService,
            ACTION_USER_INFORMATION: UserInformationDtoParser
        }
        self.function_map = {
            'GET': self.request_get,
            'POST': self.request_post,
            'PUT': self.request_put,
            'DELETE': self.request_delete
        }

    def set_json(self, json_string):
        self.json = json.loads(json_string)
        self.action = self.json[ACTION]

    def set_method(self, method):
        self.method = method

    def request_get(self):
        return self.class_map[self.action](json=self.json).request_get()

    def request_post(self):
        return self.class_map[self.action](json=self.json).request_post()

    def request_put(self):
        return self.class_map[self.action](json=self.json).request_put()

    def request_delete(self):
        return self.class_map[self.action](json=self.json).request_delete()

    def get_body(self):
        if self.action in self.class_map and self.method in self.function_map:
            return self.function_map[self.method]()
        else:
            return None
