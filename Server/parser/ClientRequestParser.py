import json

from dto.client.RegistrationDto import RegistrationDto
from dto.client.UserInformationDto import UserInformationDto
from parser.client.UserInformationDtoParser import UserInformationDtoParser
from parser.client.LoginDtoParser import LoginDtoParserService
from parser.client.RegistrationDtoParser import RegistrationDtoParserService
from resource.DtoResource import ACTION_LOGIN, ACTION_REGISTRATION, \
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
            'DELETE': self.request_delete
        }

    def set_json(self, json):
        self.json = json.loads(json_string)
        self.action = self.json[ACTION]

    def set_method(self, method):
        self.method = method

    def request_get(self):
        return self.class_map[self.action](json=self.json).request_get()

    def request_post(self):
        return self.class_map[self.action](json=self.json).request_post()

    # TODO
    def request_delete(self):
        return None

    def get_body(self):
        if self.action in self.class_map and self.method in self.function_map:
            return self.function_map[self.method]()
        else:
            return None


if __name__ == '__main__':
    #create registration json -> parse it to object
    json_string = RegistrationDto().PostRequest(
        first_name="Aleksei",
        last_name="Kop"
    ).toJSON()
    parser = ClientRequestParser(json_string=json_string, method='POST')
    request = parser.get_body()
    print request.get_data().get_first_name()

    new_json_string = UserInformationDto().GetRequest(token="ASD_TOKENADS)48735").toJSON()
    new_parser = ClientRequestParser(json_string=new_json_string, method='GET')
    new_request = new_parser.get_body()
    print new_request.get_token()
