from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


# noinspection SpellCheckingInspection
class Pile(Base):
    __tablename__ = "pile"

    id = Column("pile_id", Integer, primary_key=True)
    product_id = Column("pile_product", Integer, ForeignKey("product.product_id"))
    sell_price = Column("pile_sell", Numeric)
    buy_price = Column("pile_buy", Numeric)

    product = relationship("Product", back_populates="pile")

    def __init__(self, product, sell_price, buy_price):
        self.product = product
        self.sell_price = sell_price
        self.buy_price = buy_price
