class ProductModel(object):
	def __init__(self,transactionGen,dbConnection,dto,tk):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.dbConnection=dbConnection
		self.tk=tk
		if(dto.action=='transaction'):
			_transaction()
		elif(dto.action=='products'):
			_products()
		elif(dto.action=='product_history'):
			_product_history()
		return
	 
	def _transaction(username=None,password=None):
		return token

	def _get_session(token=None):
		statement=self.transactionGenerator("CheckSession",token)
		response=self.dbConnection.post_request(login_data)
		return

	def _products(token=None):
		return

	def _product_history(token=None):
		return
