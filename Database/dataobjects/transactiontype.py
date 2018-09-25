from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from base import Base

from transaction import Transaction


# noinspection SpellCheckingInspection
class TransactionType(Base):
    __tablename__ = "transaction_type"

    transaction_type = Column("transaction_type", String(10), primary_key=True)
    transactions = relationship(Transaction, primaryjoin=transaction_type == Transaction.transaction_type)

    def __init__(self, transaction_type):
        self.transaction_type = transaction_type
