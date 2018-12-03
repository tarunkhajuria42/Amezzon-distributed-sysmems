class Transaction_DTO(object):
	def __init__(token=None,action=None,product_action=None,
			product_id=None,product_price=None,product_quantity=None):
		self.token=token
		self.action=action
		self.product_action=action
		self.product_id=product_id
		self.product_price=product_price
		self.product_quantity=product_quantity
		
	def set_response(self,token=None,message=None,message_connection=None):
		self.token=token
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=error_messages
		reposne['data']=data
		self.response=response
		return

	def get_response():
		return json.dumps(self.response)
