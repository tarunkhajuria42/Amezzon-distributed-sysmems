from service.UserService import UserService
import uuid

class UserModel:
	def __init__(self,transactionGen,dbConnection,dto):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.us=UserService()
		self.db=dbConnection
		if(dto.action=='login'):
			response=_login(username=dto.username,password=dto.password)
		elif(dto.action=='logout'):
			response=_logout(token=dto.token)
		elif(dto.action=='get_details'):
			reponse=_get_details()
		elif(dto.action=='register'):
			reponse=_register(username=dto.username,password=dto.password,
				email=dto.email,firstname=dto.firstname,lastname=dto.lastname)
		return

	def _login(username=None,password=None):

		statement=self.transactionGenerator.getpassword(username)
		resp=db.make_transaction(statement)
		if(len(resp)==0):
			self.dto.set_response(message='wrong_input')
			return
		else:
			stored_hash=resp[0]
		if(self.us.check_password(password,stored_hash)):
			token=uuid.uuid1()
			statement=self.transactionGenerator.login(username,token)
			resp=db.make_transaction(statement)
			if():
				self.dto.response(token=token)
			else:
				self.dto.response(message='wrong_input')

	def _get_session(token=None):
		statement=self.transactionGenerator.check_session(token)	
		db.init_transaction()
		resp=db.make_transaction(statement)
		if(resp[0]):
			return resp[0]
		else:
			return False

	def _logout(token=None):
		uname=_get_session(token)
		if(uname):
			statement=self.transactionGenerator.logout(token)
			db.init_transaction()
			resp=db.make_transaction(statement)
			if(len(resp['Error'])==0):
				return True	
			else:
				return False

	def _get_details(token=None):
		uname=_get_session(token)
		if(uname):
			statement=self.transactionGenerator.get_details(username=uname)
			db.init_transaction()
			resp=db.make_transaction(statement)
			if(len(resp['Error'])==0):
				return True
		return result

	def _register(username=None, password=None, email=None,login=False,firstname=None,lastname=None):
		db.init_transaction()
		statement=self.transactionGenerator._get_user(username=username)
		resp=db.make_transaction(statement)
		if(resp==0):
			passwordHash=self.us.hash_password(password)
			statement=self.transactionGenerator._register(username=username,
				password=passwordHash,email=email,firstname=firstname,lastname=lastname)
			_login(username=username,password=password)
		else:
			self.dto.set_response(message='user_taken')

		
	def get_response():
		return self.dto




