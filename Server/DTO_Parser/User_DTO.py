import json
class User_DTO(object):
	def __init__(self,token=None,action=None,first_name=None,last_name=None,mail=None,password=None):
		self.token=token
		self.action=action
		self.first_name=first_name
		self.last_name=last_name
		self.mail=mail
		self.password=password

	def set_response(self,message=None,message_connection=None):
		self.token=token
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=error_messages
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)
