from dto.ErrorMessage import ErrorMessageList
from dto.GenericDto import GenericDto
from resource.StaticResource import ACTION_INIT_TRANSACTION


class IniTransactionDto(object):
    class GetRequest(GenericDto.CustomRequest):
        def __init__(self):
            GenericDto.CustomRequest.__init__(
                self, action=ACTION_INIT_TRANSACTION, data=self.Data(
                )
            )
        class Data(object):
            def __init__(self):
                pass

    class GetResponse(GenericDto.CustomResponse):
        def __init__(self, token=None, error_messages=None):
            GenericDto.CustomResponse.__init__(
                self, data=self.Data(
                    error_messages=error_messages
                ))
            self.token = token

        def get_token(self):
            return self.token

        def set_token(self, token):
            self.token = token

        class Data(ErrorMessageList):
            def __init__(self, error_messages=None):
                ErrorMessageList.__init__(self, error_messages=error_messages)
