class GenericO(object):
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