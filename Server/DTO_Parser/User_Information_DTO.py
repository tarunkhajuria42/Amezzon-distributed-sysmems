import json
class User_Information_DTO(object):
	def __init__(self,token=None,action=None):
		self.token=token
		self.action=action

	def set_response(self,message=None,message_connection=None,first_name=None,
							last_name=None,mail=None,username=None,id_number=None):
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=[error_messages]
		data['username']=username
		data['first_name']=first_name
		data['last_name']=last_name
		data['mail']=mail
		data['id_number']=id_number
		response['data']=data
		self.response=response
		return

	def get_response(self):
		return json.dumps(self.response)


