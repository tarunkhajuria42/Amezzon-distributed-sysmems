from model.UserModel import UserModel
from model.ProductModel import ProductModel
from service.DatabaseService import DatabaseService
from service.TransactionService import TransactionService
from DTO_Parser.DTO_Parser import DTO_Parser
class MainModel(object):
	def __init__(self,request=None):
		self.db=DatabaseService()
		self.transaction_service=TransactionService()
		dto=DTO_Parser(request)
		aciton=dto.action
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
		else:
			self.response="ERROR_BAD_REQUEST"
		dto=model.response()
		self.response=dto.get_response()
		return
	def response(self):
		return self.response
