from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from base import Base
from product import Product


# noinspection SpellCheckingInspection
class ProductType(Base):
    __tablename__ = "product_type"

    product_type = Column(String(10), primary_key=True)

    products = relationship(Product, primaryjoin=product_type == Product.product_type)

    def __init__(self, product_type):
        self.product_type = product_type
