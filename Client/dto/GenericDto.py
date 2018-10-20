import json


class GenericDto(object):
    class CustomRequest(object):
        def __init__(self, action=None, data=None):
            self.action = action
            self.data = data

        def get_action(self):
            return self.action

        def set_action(self, action):
            self.action = action

        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = data

        def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

    class CustomAuthRequest(object):
        def __init__(self, action=None, token=None, data=None):
            self.action = action
            self.token = token
            self.data = data

        def get_action(self):
            return self.action

        def set_action(self, action):
            self.action = action

        def get_token(self):
            return self.token

        def set_token(self, token):
            self.token = token

        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = data

        def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

    class CustomResponse(object):
        def __init__(self, data=None):
            self.data = data

        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = data

        def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)
