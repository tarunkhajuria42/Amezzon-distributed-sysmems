from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


# noinspection SpellCheckingInspection
class Transaction(Base):
    __tablename__ = "transaction"

    id = Column("transaction_id", Integer, primary_key=True)
    transaction_type = Column("transaction_type", String(10), ForeignKey("transactiontype.transaction_type"))
    transaction_client = Column("transaction_client", Integer, ForeignKey("person.person_id"))
    transaction_product = Column("transaction_product", Integer, ForeignKey("product.product_id"))
    transaction_price = Column("transaction_price", Numeric)
    transaction_quantity = Column("transaction_quantity", Integer)
    transaction_timestamp = Column("transaction_timestamp", DateTime)

    type = relationship("TransactionType", back_populates="transactions")
    client = relationship("Person", back_populates="transactions")
    product = relationship("Product")
