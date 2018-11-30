class Login_DTO(object):
	def __init__(username=None,password=None,action=action):
		self.username=username
		self.password=password
		self.action=action
	def set_response(self,token=token,message=None,message_connection=None):
		self.token=token
		response={}
		data={}
		error_messages={}
		error_messages['message']=message
		error_messages['message_connection']=message_connection
		data['error_messages']=error_messages
		data['token']=token
		reposne['data']=data
		self.response=response
		return

	def get_response():
		return json.dumps(self.response)


