from dto.client.LoginDto import LoginDto
from parser.client.GenericDtoParser import GenericDtoParser
from resource.DtoResource import DATA, USERNAME, PASSWORD


class LoginDtoParserService(GenericDtoParser):
    def request_post(self):
        return LoginDto().PostRequest(
            username=self.json[DATA][USERNAME],
            password=self.json[DATA][PASSWORD]
        )

    # TODO
    def response_post(self):
        return None
