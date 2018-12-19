from service.TransactionService import TransactionService 
import time
f = '%Y-%m-%d %H:%M:%S'
class ProductModel(object):
	def __init__(self,transactionGen,dbConnection,dto,tk):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.db=dbConnection
		self.tk=tk
		if(dto.action=='transaction'):
			self._transaction(token=dto.token,
				product_id=dto.product_id,
				buy_price=dto.buy_price,
				sell_price=dto.sell_price,
				product_quantity=dto.product_quantity,
				product_action=dto.product_action)
		elif(dto.action=='products'):
			self._products(token=dto.token)
		elif(dto.action=='product_by_id'):
			self._get_one_product(token=dto.token,product_id=dto.product_id)
		elif(dto.action=='product_history'):
			self._product_history()
		return
	 
	def _transaction(self,token=None,product_id=None,buy_price=None,sell_price=None, product_quantity=None,product_action=None):
		user=self._get_session(token=token)
		transaction_service=TransactionService()
		if(user):
			db_token=self.db.init_transaction()
			statement=self.transactionGenerator.get_user_id(username=user)
			resp=self.db.make_transaction_commit(data=statement,token=db_token)
			if(len(resp['Error'])!=0):
				self.dto.set_response(message='system_error',message_connection='transaction')
				return 
			user_id=resp['Result']['rows'][0][0]
			db_token=self.db.init_transaction()
			statement=self.transactionGenerator.get_prices_quantity(product_id = product_id)
			resp=self.db.make_transaction(data=statement,token=db_token)
			if(len(resp['Error'])!=0):
				self.dto.set_response(message='system_error',message_connection='trasaction')
				return
			base_sell=float(resp['Result']['rows'][0][0])
			base_buy=float(resp['Result']['rows'][0][1])
			previous_quantity=int(resp['Result']['rows'][0][2])
			if(product_action == 'BUY'):
				if(previous_quantity<int(product_quantity)):
					self.dto.set_response(message='less_quantity',
						message_connection='transaction',
						quantity=previous_quantity,
						sell_price=resp['Result']['rows'][0][3],
						buy_price=resp['Result']['rows'][0][4]
						)
					return
				new_quantity=previous_quantity - int(product_quantity)
				new_prices=transaction_service.buy(buyPrice=float(buy_price),
					previous_quantity=previous_quantity,
					amount=int(product_quantity),
					sellPrice=float(sell_price),
					base_buy=base_buy,
					base_sell=base_sell)
				price=float(buy_price)
				product_action='BUYING'
			else:
				new_prices=transaction_service.sell(buyPrice=float(buy_price),
					previous_quantity=previous_quantity,
					amount=int(product_quantity),
					sellPrice=float(sell_price),
					base_buy=base_buy,
					base_sell=base_sell)
				price=float(sell_price)
				new_quantity=previous_quantity+int(product_quantity)
				product_action='SELLING'
			time_stamp=time.strftime(f)
			statement=self.transactionGenerator.set_transaction(user_id=user_id,
				price=price,
				transaction_type=product_action,
				product_id=product_id,
				quantity=int(product_quantity),
				timestamp=time_stamp)
			resp1=self.db.make_transaction(data=statement,token=db_token)
			statement=self.transactionGenerator.set_product_history(product_id=product_id,
				buy_price=new_prices[0],
				sell_price=new_prices[1],
				quantity=new_quantity,
				timestamp=time_stamp)
			resp2=self.db.make_transaction_commit(data=statement,token=db_token)
			if(len(resp1['Error'])+len(resp2['Error'])==0):
				self.dto.set_response(buy_price=new_prices[0],sell_price=new_prices[1],quantity=new_quantity)
			else:
				self.dto.set_response(message='system_error',message_connection='trasaction',
					buy_price=resp['Result']['rows'][0][3],sell_price=resp['Result']['rows'][0][4],
					quantity=previous_quantity)
		else:
			self.dto.set_response(message='invalid_user',message_connection='transaction')
		return 

	def _get_session(self,token=None):
		resp=self.tk.retrieve_user(token=token)
		return resp

	def _get_one_product(self,token=None,product_id=None):
		user=self._get_session(token=str(token))
		if(user):
			statement=self.transactionGenerator.get_one_product(product_id)
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
					product['product_quantity']=float(row[4])
					product['buy_price']=float(row[6])
					product['sell_price']=float(row[5])
					product_list.append(product)
				self.dto.set_response(product_list=product_list)
			else:
				self.dto.set_response(message='system_error',message_connection='product')			
		else:
			self.dto.set_response(message='invalid token',message_connection='product')
		return
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
					product['product_quantity']=float(row[4])
					product['buy_price']=float(row[6])	
					product['sell_price']=float(row[5])
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
