import json
class Transaction_DTO(object):
	def __init__(self,token=None,action=None,product_action=None,
			product_id=None,buy_price=None,sell_price=None,product_quantity=None):
		self.token=token
		self.action=action
		self.product_action=product_action	
		self.product_id=product_id
		self.buy_price=buy_price
		self.sell_price=sell_price
		self.product_quantity=product_quantity
		
	def set_response(self,message=None,message_connection=None,buy_price=None,sell_price=None,quantity=None):
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=[error_messages]
		data['buy_price']=buy_price
		data['sell_price']=sell_price
		data['quantity']=quantity
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)
