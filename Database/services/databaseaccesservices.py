from dataobjects.dataobjects import *


def username_exists(username, session):
    return session.query(Person).filter(Person.username == username).count() > 0


def username_authentication_correct(username, password_hash, session):
    return session.query(Person).filter(Person.username == username & Person.password_hash == password_hash).count() > 0


def get_user_by_username(username, session):
    return session.query(Person).filer(Person.username == username).one()
