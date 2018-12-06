class Product_History_DTO():
	def __init__(self,token=None,product_id=None,
			start_datetime=None,action=None):
		self.token=token
		self.product_id=product_id
		self.action=action
		self.start_datetime=start_datetime

	def set_response(self,token=None,message=None,message_connection=None):
		self.token=token
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=error_messages
		data['transaction_price_history']=transaction_price_history
		data['product_quantity']=product_quantity
		data['buy_price']=buy_price
		data['time_stamp']=time_stamp
		reposne['data']=data
		self.response=response
		return
		
	def get_response(self):
		return json.dumps(self.response)


