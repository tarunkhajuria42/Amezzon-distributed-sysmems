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
	 
	def _transaction(self,token=None):
		self._get_session(token=token)

		return token

	def _get_session(self,token=None):
		resp=self.tk.make_transaction(token=token)
		return resp

	def _products(self,token=None):
		return

	def _product_history(self,token=None):
		return
