from domain.GenericModel import GenericModel


class ErrorMessageList(object):
    def __init__(self, error_messages=None):
        if error_messages is None:
            error_messages = []
        self.error_messages = error_messages

    def get_error_messages(self):
        return self.error_messages

    def set_error_messages(self, error_messages):
        self.error_messages = error_messages

    def add_error_message(self, message_connection, message):
        self.error_messages.append(
            ErrorMessage(message_connection=message_connection, message=message)
        )


class ErrorMessage(GenericModel):
    def __init__(self, message_connection=None, message=None):
        self.message_connection = message_connection
        self.message = message

    def get_type(self):
        return self.message_connection

    def set_type(self, type):
        self.message_connection = type

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message
