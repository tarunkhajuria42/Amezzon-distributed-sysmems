
class UserModel:
	def __init__(self,transactionGen,dbConnection,dto):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.dbConnection=dbConnection
		#initialise queryGenerator
		#initiliase Database Connection
		return

	def login(username=None,password=None):
		login_data=self.transactionGenerator("",username,password)
		self.dbConnection.post_request(login_data)
		return token

	def get_session(token=None):
		login_data=self.transactionGenerator("Session",token)
		response=self.dbConnection.post_request(login_data)
		return

	def logout(token=None):

		return

	def get_details(token=None):
		return

