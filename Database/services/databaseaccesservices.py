from services.dataobjects.dataobjects import *


def username_exists(username, session):
    return session.query(Person).filter(Person.username == username).count() > 0


def username_authentication_correct(username, password_hash, session):
    return session.query(Person).filter(Person.username == username & Person.password_hash == password_hash).count() > 0


def get_user_by_username(username, session):
    return session.query(Person).filter(Person.username == username).one()


def get_new_user(username, password_hash, first_name, last_name, session):
    person = Person(username, password_hash, first_name, last_name)
    session.save(person)
    session.flush()
    return person


def add_new_person(person, session):
    session.save(person)
    session.flush()
