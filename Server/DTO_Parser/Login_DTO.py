
import json
class Login_DTO(object):
	def __init__(self,username=None,password=None,action=None):
		self.username=username
		self.password=password
		self.action=action
	
	def set_response(self,token=None,message=None,message_connection=None):
		self.token=token
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=[error_messages]
		data['token']=token
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)


