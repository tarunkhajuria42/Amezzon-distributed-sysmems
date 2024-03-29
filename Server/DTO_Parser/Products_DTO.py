import json
class Products_DTO(object):
	def __init__(self,action=None,token=None,product_id=None):
		self.action=action
		self.token=token
		self.product_id=product_id

	def set_response(self,token=None,message=None,message_connection=None,product_list=None,response_date_time=None):
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=[error_messages]
		data['product_list']=product_list
		data['response_date_time']=response_date_time
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)


