from math import exp
from random import uniform
class TransactionService(object):
	def __init__(self):
		return

	def buy(self,sellPrice=None,buyPrice=None,previous_quantity=None,amount=None,base_buy=None,base_sell=None):
		amount=float(amount)
		previous_quantity=float(previous_quantity)
		ratio=min(float(amount/previous_quantity),1)
		bp=max(buyPrice+(buyPrice*ratio),base_buy)
		sp=min(bp*0.75,base_sell)
		return [bp,sp]

	def sell(self,sellPrice=None,buyPrice=None,previous_quantity=None,amount=None,base_buy=None,base_sell=None):
		amount=float(amount)
		previous_quantity=float(previous_quantity)
		ratio=min(amount/previous_quantity,1)
		sp=min(sellPrice-(sellPrice*ratio),base_sell)
		bp=max(sp*1.25,base_buy)
		return [bp,sp]
