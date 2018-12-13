import json
class Logout_DTO(object):
	def __init__(self,token=None,action=None):
		self.token=token
		self.action=action
		
	def set_response(self,message=None,message_connection=None):
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=[error_messages]
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)
