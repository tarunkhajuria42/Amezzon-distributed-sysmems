from dto.client.RegistrationDto import RegistrationDto
from parser.client.GenericDtoParser import GenericDtoParser
from resource.StaticResource import DATA, LOGIN, USERNAME, PASSWORD, \
    FIRST_NAME, LAST_NAME, MAIL, ID_CODE


class RegistrationDtoParserService(GenericDtoParser):
    def request_post(self):
        return RegistrationDto().PostRequest(
            login=self.json[LOGIN],
            username=self.json[DATA][USERNAME],
            password=self.json[DATA][PASSWORD],
            first_name=self.json[DATA][FIRST_NAME],
            last_name=self.json[DATA][LAST_NAME],
            mail=self.json[DATA][MAIL],
            id_code=self.json[DATA][ID_CODE]
        )

    # TODO
    def response_post(self):
        return None
