from math import exp
from random import uniform
class TransactionService(object):
	def __init__():
		return

	def buy(sellPrice=None,buyPrice=None,previous_qunatity=None,amount=None):
		self.D=amount/previous_qunatity
		self.S=1-(amount/previous_qunatity)
		bp=min(buyPrice*(1+exp(self.D-1)),buyPrice)
		sp=max(bp*uniform(1.05,1.35),sellPrice)
		return [bp,sp]

	def sell(sellPrice=None,buyPrice=None,previous_qunatity=None,amount=None):
		self.D=amount/previous_qunatity
		self.S=1-(amount/previous_qunatity)
		sp=max(sellPrice*exp(-self.S),sellPrice)
		bp=min(sp*uniform(0.75,0.99),buyPrice)
		return [bp,sp]
