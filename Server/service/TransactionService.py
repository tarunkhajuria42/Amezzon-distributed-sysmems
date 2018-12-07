from math import exp
from random import uniform
class TransactionService(object):
	def __init__(self):
		return

	def buy(self,sellPrice=None,buyPrice=None,previous_qunatity=None,amount=None,base_buy=None,base_sell=None):
		self.D=amount/previous_qunatity
		self.S=1-(amount/previous_qunatity)
		bp=min(buyPrice*(1+exp(self.D-1)),base_buy)
		sp=max(bp*uniform(1.05,1.35),base_sell)
		return [bp,sp]

	def sell(self,sellPrice=None,buyPrice=None,previous_qunatity=None,amount=None,base_buy=None,base_sell=None):
		self.D=amount/previous_qunatity
		self.S=1-(amount/previous_qunatity)
		sp=max(sellPrice*exp(-self.S),base_sell)
		bp=min(sp*uniform(0.75,0.99),base_buy)
		return [bp,sp]
