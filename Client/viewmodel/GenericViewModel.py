class GenericViewModel(object):
    def __init__(self, error_message=None):
        self.error_message = error_message

    def get_error_message(self):
        return self.error_message

    def set_error_message(self, error_message):
        self.error_message = error_message

    def __eq__(self, other):
        eq = True
        for attribute in self.__dict__:
            try:
                if self.__getattribute__(attribute) != other.__getattribute__(attribute):
                    eq = False
            except AttributeError:
                return False
        return eq

    def __ne__(self, other):
        return not self.__eq__(other=other)

    def __repr__(self):
        return str(self.__dict__)
