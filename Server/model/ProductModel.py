class ProductModel(object):
	def __init__(self,transactionGen,dbConnection,dto,tk):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.db=dbConnection
		self.tk=tk
		if(dto.action=='transaction'):
			self._transaction()
		elif(dto.action=='products'):
			self._products(token=dto.token)
		elif(dto.action=='product_history'):
			self._product_history()
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

	def _get_one_product(self,token=None,product_id=None):
		if(user):
			statement=self.transactionGenerator.get_one_product(product_id)
			db_token=self.db.init_transaction()
			resp=self.db.make_transaction_commit(data=statement,token=db_token)
			if(len(resp['Error'])!=0):
				print(resp['Results'])
		self.dto.set_response()
		return

	def _products(self,token=None):
		user=self._get_session(token=str(token))
		if(user):
			statement=self.transactionGenerator.get_products()
			db_token=self.db.init_transaction()
			resp=self.db.make_transaction_commit(data=statement,token=db_token)
			if(len(resp['Error'])==0):
				product_list=[]
				for row in resp['Result']['rows']:
					product={}
					product['product_id']=int(row[0])
					product['product_name']=row[1]
					product['type']=row[2]
					product['product_description']=row[3]
					product['product_quantity']=row[4]
					product['buy_price']=row[6]
					product['sell_price']=row[5]
					product_list.append(product)
				self.dto.set_response(product_list=product_list)
			else:
				self.dto.set_response(message='system_error',message_connection='product')			
		else:
			self.dto.set_response(message='invalid token',message_connection='product')
		return

	def _product_history(self,token=None):
		return

	def get_response(self):
		return self.dto
