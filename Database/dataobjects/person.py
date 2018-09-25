from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


# noinspection SpellCheckingInspection
class Person(Base):
    __tablename__ = "person"

    id = Column("person_id", Integer, primary_key=True)
    username = Column("person_username", String(40))
    passwordhash = Column("person_passwordhash", String(40))
    first_name = Column("person_firstname", String(50))
    last_name = Column("person_lastname", String(250))
    mail = Column("person_mail", String(250))

    transactions = relationship("Transaction")

    def __init__(self, username, passwordhash, first_name, last_name, mail):
        self.username = username
        self.passwordhash = passwordhash
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
