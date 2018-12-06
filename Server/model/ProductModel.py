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
	 
	def _transaction(self,):
		return token

	def _get_session(self,token=None):
		statement=self.transactionGenerator("CheckSession",token)
		response=self.dbConnection.post_request(login_data)
		return

	def _products(self,token=None):
		return

	def _product_history(self,token=None):
		return
