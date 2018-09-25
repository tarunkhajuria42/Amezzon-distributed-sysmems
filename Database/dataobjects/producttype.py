from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from base import Base


# noinspection SpellCheckingInspection
class ProductType(Base):
    __tablename__ = "product_type"

    product_type = Column(String(10), primary_key=True)

    products = relationship("Product")

    def __init__(self, product_type):
        self.product_type = product_type
