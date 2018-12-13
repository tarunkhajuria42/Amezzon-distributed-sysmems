from dto.GenericDto import GenericDto
from resource.StaticResource import ACTION_LOGOUT


class LogoutDto(object):
    class GetRequest(GenericDto.CustomAuthRequest):
        def __init__(self, token=None):
            GenericDto.CustomAuthRequest.__init__(
                self, action=ACTION_LOGOUT, token=token,
                data=self.Data()
            )

        class Data(object):
            def __init__(self):
                pass
