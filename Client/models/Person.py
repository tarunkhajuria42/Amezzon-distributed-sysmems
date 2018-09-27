class Person(object):
    def __init__(self, id=None, first_name=None, last_name=None, email=None, id_code=None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._id_code = id_code

    @property
    def id(self):
        return self._id

    @id.getter
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @first_name.deleter
    def first_name(self):
        del self._first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.getter
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @last_name.deleter
    def last_name(self):
        del self._last_name

    def get_full_name(self):
        return "{0} {1}".format(self._first_name, self._last_name)

    @property
    def email(self):
        return self._email

    @email.getter
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @email.deleter
    def email(self):
        del self._email

    @property
    def id_code(self):
        return self._id_code

    @id_code.getter
    def id_code(self):
        return self._id_code

    @id_code.setter
    def id_code(self, id_code):
        self._id_code = id_code

    @id_code.deleter
    def id_code(self):
        del self._id_code

    def __eq__(self, other):
        return (self._first_name == other.first_name and
                self._last_name == other.last_name and
                self._email == other.email and
                self._id_code == other.id_code)
