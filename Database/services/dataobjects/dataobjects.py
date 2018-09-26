from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://testuser@localhost/amezzon")  # TODO switch to configParser
Session = sessionmaker(bind=engine)
__BASE = declarative_base()


# noinspection SpellCheckingInspection
class Person(__BASE):
    __tablename__ = "person"

    __id = Column("person_id", Integer, primary_key=True)
    username = Column("person_username", String(40))
    password_hash = Column("person_passwordhash", String(40))
    first_name = Column("person_firstname", String(50))
    last_name = Column("person_lastname", String(250))
    mail = Column("person_mail", String(250))

    def __init__(self, username, passwordhash, first_name, last_name, mail):
        self.username = username
        self.password_hash = passwordhash
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail

    def __eq__(self, other):
        return eq(self.__id, other.__id)

    def __str__(self):
        return "Person: " + str({k: self.__dict__[k] for k in ("username", "first_name", "last_name")})


# noinspection SpellCheckingInspection
class Pile(__BASE):
    __tablename__ = "pile"

    id = Column("pile_id", Integer, primary_key=True)
    product_id = Column("pile_product", Integer, ForeignKey("product.product_id"))
    sell_price = Column("pile_sell", Numeric)
    buy_price = Column("pile_buy", Numeric)

    def __init__(self, product, sell_price, buy_price):
        self.product = product
        self.sell_price = sell_price
        self.buy_price = buy_price

    def __eq__(self, other):
        return eq(self.id, other.id)

    def __str__(self):
        return "Pile: " + str({k: self.__dict__[k] for k in "product_id"})


class Product(__BASE):
    __tablename__ = "product"

    id = Column("product_id", Integer, primary_key=True)
    product_type = Column("product_type", String(10), ForeignKey("product_type.product_type"))
    product_name = Column("product_name", String(50))
    description = Column("product_description", String(255))

    def __init__(self, product_type, product_name, description):
        self.product_type = product_type
        self.product_name = product_name
        self.description = description

    def __eq__(self, other):
        return eq(self.id, other.id)

    def __str__(self):
        return "Product: " + str({k: self.__dict__[k] for k in ("product_name", "product_type")})


class ProductType(__BASE):
    __tablename__ = "product_type"

    product_type = Column(String(10), primary_key=True)

    def __init__(self, product_type):
        self.product_type = product_type

    def __eq__(self, other):
        return eq(self.product_type, other.product_type)

    def __str__(self):
        return "ProductType: " + str(self.__dict__)


# noinspection SpellCheckingInspection
class Transaction(__BASE):
    __tablename__ = "transaction"

    id = Column("transaction_id", Integer, primary_key=True)
    transaction_type = Column("transaction_type", String(10), ForeignKey("transaction_type.transaction_type"))
    transaction_client = Column("transaction_client", Integer, ForeignKey("person.person_id"))
    transaction_product = Column("transaction_product", Integer, ForeignKey("product.product_id"))
    transaction_price = Column("transaction_price", Numeric)
    transaction_quantity = Column("transaction_quantity", Integer)
    transaction_timestamp = Column("transaction_timestamp", DateTime)

    def __init__(self, transaction_type, client, product, price, quantity, timestamp):
        self.transaction_type = transaction_type
        self.transaction_client = client
        self.transaction_product = product
        self.transaction_price = price
        self.transaction_quantity = quantity
        self.transaction_timestamp = timestamp

    def __eq__(self, other):
        return eq(self.id, other.id)

    def __str__(self):
        return "Transaction: " + str(self.__dict__)  # TODO specify


# noinspection SpellCheckingInspection
class TransactionType(__BASE):
    __tablename__ = "transaction_type"

    transaction_type = Column("transaction_type", String(10), primary_key=True)

    def __init__(self, transaction_type):
        self.transaction_type = transaction_type

    def __eq__(self, other):
        return eq(self.transaction_type, other.transaction_type)

    def __str__(self):
        return "TransactionType: " + str(self.__dict__)


__BASE.metadata.create_all(engine)
