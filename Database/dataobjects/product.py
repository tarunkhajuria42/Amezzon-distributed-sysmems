from sqlalchemy import Column, Integer, String
from base import Base


class Product(Base):
    __tablename__ = "product"

    id = Column("product_id", Integer, primary_key=True)
