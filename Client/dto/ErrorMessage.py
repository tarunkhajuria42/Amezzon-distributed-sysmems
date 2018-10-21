from domain.GenericModel import GenericModel


class ErrorMessages(object):
    def __init__(self, error_messages=None):
        if error_messages is None:
            self.error_messages = [Message()]
        else:
            self.error_messages = error_messages

    def get_error_messages(self):
        return self.error_messages

    def set_error_messages(self, error_messages):
        self.error_messages = error_messages

    def add_error_message(self, type, message):
        self.error_messages.append(
            Message(type=type, message=message)
        )


class Message(GenericModel):
    def __init__(self, type=None, message=None):
        self.type = type
        self.message = message

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message
