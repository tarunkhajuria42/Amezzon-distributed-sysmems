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
	 
	def _transaction(self,token=None,product_id=None,product_price=None, product_quantity=None,product_action=None):
		user=self._get_session(token=token)
		if(user):
			if(product_action == 'BUY'):
				statement=self.transactionGenerator.get_prices(product_id = product_id)
				db_token=self.db.init_transaction()
				resp=self.db.make_transaction_commit(data = statement,token = db_token)
				
 				
			

		return token

	def _get_session(self,token=None):
		resp=self.tk.retrieve_user(token=token)
		return resp

	def _products(self,token=None,product_id=None):
		user=self._get_session(token=token)
		if(user):
			statement=self.transactionGenerator.get_products(product_id)
			db_token=self.db.init_transaction()
			resp=self.db.make_transaction_commit(data=statement,token=db_token)
			if(len(rep['Error'])!=0):
				a=1







		return

	def _product_history(self,token=None):
		return
