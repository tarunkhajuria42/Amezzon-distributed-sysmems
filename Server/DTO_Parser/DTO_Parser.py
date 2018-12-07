""" Parser to convert data into relevant dto"""
import json
from Login_DTO import Login_DTO
from Logout_DTO import Logout_DTO
from Product_History_DTO import Product_History_DTO
from Transaction_DTO import Transaction_DTO
from Products_DTO import Products_DTO
from Registration_DTO import Registration_DTO
from User_Information_DTO import User_Information_DTO
from User_DTO import User_DTO

class DTO_Parser(object):
	def __init__(self,request_string):
		self.req=json.loads(request_string)
		if(self.req['action']):
			action=self.req['action']
			if(action=='login'):
				self._login()
			elif(action=='logout'):
				self._logout()
			elif(action=='product_history'):
				self._product_history()
			elif(action=='transaction'):
				self._transaction()
			elif(action=='products'):
				self._products()
			elif(action=='registration'):
				self._registration()
			elif(action=='user_information'):
				self._user_information()
			elif(action=='user'):
				self._user()

#Todo Put checks
	def _login(self):
		data=self.req['data']
		action=self.req['action']	
		self.DTO=Login_DTO(username=data['username'],password=data['password'],action=action)
		return
	def _logout(self):
		data=self.req['data']	
		token=self.req['token']
		action=self.req['action']
		self.DTO=Logout_DTO(token=token,action=action)
		return
	def _product_history(self):
		data=self.req['data']
		token=self.req['token']
		action=self.req['action']	
		self.DTO=Product_History_DTO(token=token,product_id=data['product_id'],
			start_datetime=data['start_datetime'],action=action)
		return
	def _transaction(self):
		data=self.req['data']
		token=self.req['token']
		action=self.req['action']		
		self.DTO=Transaction_DTO(token=token,action=action,product_action=data['action'],
			product_id=data["product_id"],product_price=data["product_price"],product_quantity=data["product_quantity"])
		return
	def _products(self):
		data=self.req['data']
		action=self.req['action']
		token=self.req['token']	
		self.DTO=Products_DTO(token=token,action=action)
		return
	def _registration(self):
		data=self.req['data']
		action=self.req['action']
		login=self.req['login']	
		self.DTO=Registration_DTO(action=action,login=login,username=data['username'],password=data['password'],
			first_name=data['first_name'],last_name=data['last_name'],mail=data['mail'],id_code=data['id_code'])
		return
	def _user_information(self):
		action=self.req['action']
		token=self.req['token']	
		self.DTO=User_Information_DTO(action=action,token=token)
		return
	def _user(self):
		data=self.req['data']
		action=self.req['action']	
		self.DTO=User_DTO(action=action,token=token,first_name=data['first_name'],
			last_name=data['last_name'],mail=data['mail'],password=data['password'])
		return
	def get_DTO(self):	
		return self.DTO


