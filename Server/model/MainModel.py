from model.UserModel import UserModel
from model.ProductModel import ProductModel
from manager.DatabaseManager import DatabaseManager
from service.TransactionService import TransactionService
class MainModel(object):
	def __init__(self,request=None):
		self.db=DatabaseManager()
		self.transaction_service=TransactionService()
		dto=Parser(request)
		aciton=dto.get_action()
		if(action=='login'):
			model=UserModel(self.transaction_service,self.db,dto)
		elif(action=='logout'):
			model=UserModel(self.transaction_service,self.db,dto)
		elif(action=='product_history'):
			model=ProductModel(self.transaction_service,self.db,dto)
		elif(action=='transaction'):
			model=ProductModel(self.transaction_service,self.db,dto)
		elif(action=='products'):
			model=ProductModel(self.transaction_service,self.db,dto)
		elif(action=='registration'):
			model=UserModel(self.transaction_service,self.db,dto)
		elif(action=='user_information'):
			model=UserModel(self.transaction_service,self.db,dto)
		elif(action=='user'):
			model=UserModel(self.transaction_service,self.db,dto)
		dto=model.response()
		self.response=dto.toJSON()
		return
	def response(self):
		return self.response
