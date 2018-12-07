import json
class Products_DTO(object):
	def __init__(self,action=None,token=None):
		self.action=action
		self.token=token

	def set_response(self,token=None,message=None,message_connection=None,product_list=None,response_date_time=None):
		self.token=token
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=error_messages
		data['product_list']=product_list
		data['response_date_time']=response_date_time
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)


