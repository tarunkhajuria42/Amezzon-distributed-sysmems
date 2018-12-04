from model.UserModel import UserModel
from model.ProductModel import ProductModel
from service.DatabaseService import DatabaseService
from DBStatements.DatabaseStatement import DatabaseStatement
from DTO_Parser.DTO_Parser import DTO_Parser
from service.TokenService import TokenService
class MainModel(object):
	def __init__(self,request=None):
		self.db=DatabaseService()
		self.transaction_service=DatabaseStatement()
		self.tk=TokenService()
		dto=DTO_Parser(request).get_DTO()
		action=dto.action
		if(action=='login'):
			model=UserModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='logout'):
			model=UserModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='product_history'):
			model=ProductModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='transaction'):
			model=ProductModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='products'):
			model=ProductModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='registration'):
			model=UserModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='user_information'):
			model=UserModel(self.transaction_service,self.db,dto,self.tk)
		elif(action=='user'):
			model=UserModel(self.transaction_service,self.db,dto,self.tk)
		else:
			self.response="ERROR_BAD_REQUEST"
		dto=model.get_response()
		self.response=dto.get_response()
		return

	def get_response(self):
		return self.response
