from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

from pile import Pile


# noinspection SpellCheckingInspection
class Product(Base):
    __tablename__ = "product"

    id = Column("product_id", Integer, primary_key=True)
    product_type = Column("product_type", String(10), ForeignKey("product_type.product_type"))
    product_name = Column("product_name", String(50))
    description = Column("product_description", String(255))

    pile = relationship(Pile, primaryjoin=id == Pile.product_id)

    def __init__(self, product_type, product_name, description):
        self.product_type = product_type
        self.product_name = product_name
        self.description = description
