class ProductModel(object):
	def __init__(self,transactionGen,dbConnection,dto):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.dbConnection=dbConnection
		if(dto.action=='transaction'):
			_login()
		elif(dto.action=='products'):
			_logout()
		elif(dto.action=='product_history'):
			_product_history()
		return

	def _login(username=None,password=None):
		return token

	def _get_session(token=None):
		statement=self.transactionGenerator("CheckSession",token)
		response=self.dbConnection.post_request(login_data)
		return

	def _logout(token=None):
		return

	def _get_details(token=None):
		return

	def get_response():
		return self.dto
