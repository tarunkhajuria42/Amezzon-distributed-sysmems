from dto.client.UserInformationDto import UserInformationDto
from parser.client.GenericDtoParser import GenericDtoParser
from resource.StaticResource import TOKEN, FIRST_NAME, LAST_NAME, MAIL, PASSWORD


class UserInformationDtoParser(GenericDtoParser):
    def request_get(self):
        return UserInformationDto().GetRequest(
            token=self.json[TOKEN]
        )

    # TODO
    def response_get(self):
        return None

    def request_post(self):
        return UserInformationDto().PostRequest(
            token=self.json[TOKEN],
            first_name=self.json[FIRST_NAME],
            last_name=self.json[LAST_NAME],
            mail=self.json[MAIL],
            password=self.json[PASSWORD]
        )

    # TODO
    def response_post(self):
        return None