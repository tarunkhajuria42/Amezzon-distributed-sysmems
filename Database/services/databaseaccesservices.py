from services.dataobjects.dataobjects import *


class DatabaseAccessService(object):

    def __init__(self):
        pass

    def username_exists(self, username, session):
        return session.query(Person).filter(Person.username == username).count() > 0

    def username_authentication_correct(self, username, password_hash, session):
        return session.query(Person).filter(
            Person.username == username & Person.password_hash == password_hash).count() > 0

    def get_user_by_username(self, username, session):
        return session.query(Person).filter(Person.username == username).one()

    def get_new_user(self, username, password_hash, first_name, last_name, session):
        person = Person(username, password_hash, first_name, last_name)
        session.save(person)
        session.flush()
        return person

    def add_new_person(self, person, session):
        session.save(person)
        session.flush()
