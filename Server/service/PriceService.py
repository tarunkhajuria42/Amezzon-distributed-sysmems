import numpy as np
import math

class PriceService:
	def __init__(self,price_buy=None,price_sell=None,base_buy=None,base_sell=None):
		self.base_sell=base_sell
		self.base_buy=base_buy
		self.price_buy=price_buy
		self.price_sell=price_sell

	def set_prices(self,price_buy=None,price_sell=None):
		if(price_buy):
			self.price_buy=price_buy
		if(price_sell):
			self.price_sell=price_sell
	def update_prices_sell(q=None,dq=None):
		S=1-(dq/q)
		self.price_sell=max(self.price_sell*exp(-S),self.base_sell)
		self.price_buy=min(self.price_sell*np.random.normal(0.75,0.99),self.base_buy)
		return True
	def update_prices_buy(q=None,dq=None):
		D=dq/q
		self.price_buy=min(self.price_buy*(1+math.exp(D-1),self.base_buy))
		self.price_sell=max(self.price_buy*np.random.normal(1.05,1.35),self.base_sell)
		return True

	def get_price_buy(self):
		return self.price_buy

	def get_price_sell(self):
		return self.price_sell




