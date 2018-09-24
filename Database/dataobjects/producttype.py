from sqlalchemy import Column, String
from base import Base


# noinspection SpellCheckingInspection
class ProductType(Base):
    __tablename__ = "product_type"

    product_type = Column(String(10), primary_key=True)

    def __init__(self, product_type):
        self.product_type = product_type
