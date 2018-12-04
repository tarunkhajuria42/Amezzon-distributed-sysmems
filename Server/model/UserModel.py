from service.UserService import UserService
import uuid

class UserModel:
	def __init__(self,transactionGen,dbConnection,dto,tk):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.us=UserService()
		self.db=dbConnection
		self.tk=tk
		print(dto.action)
		if(dto.action=='login'):
			response=self._login(username=dto.username,password=dto.password)
		elif(dto.action=='logout'):
			response=self._logout(token=dto.token)
		elif(dto.action=='get_details'):
			reponse=self._get_details()
		elif(dto.action=='registration'):
			reponse=self._register(username=dto.username,password=dto.password,
				mail=dto.mail,firstname=dto.firstname,lastname=dto.lastname)
		return

	def _login(self,username=None,password=None):
		t_token=self.db.init_transaction()	
		statement=self.transactionGenerator.getpassword(username)
		resp=self.db.make_transaction(data=statement,token=t_token)
		print(resp['Result']['rows'][0])
		if(resp['Result']['rows'][0]):
			self.dto.set_response(message='wrong_input')
			return
		else:
			stored_hash=resp[0]
		if(self.us.check_password(password,stored_hash)):
			token=uuid.uuid1()
			statement=self.transactionGenerator.login(username,token)
			resp=self.db.make_transaction(statement)
			if(len(resp['Error'])==0):
				self.dto.response(token=token)
		else:
			self.dto.response(message='wrong_input')

	def _get_session(self,token=None):
		statement=self.transactionGenerator.check_session(token)	
		dk.init_transaction()
		resp=tk.make_transaction(statement)
		if(resp[0]):
			return resp[0]
		else:
			return False

	def _logout(self,token=None):
		uname=_get_session(token)
		if(uname):
			statement=self.transactionGenerator.logout(token)
			self.db.init_transaction()
			resp=db.make_transaction(statement)
			if(len(resp['Error'])==0):
				return True	
			else:
				return False

	def _get_details(self,token=None):
		uname=_get_session(token)
		if(uname):
			statement=self.transactionGenerator.get_details(username=uname)
			self.db.init_transaction()
			resp=self.db.make_transaction(statement)
			if(len(resp['Error'])==0):
				return True
		return result

	def _register(self,username=None, password=None, mail=None,login=False,firstname=None,lastname=None):
		t_token=self.db.init_transaction()
		statement=self.transactionGenerator.get_user(username=username)
		resp=self.db.make_transaction(data=statement,token=t_token)
		if(len(resp['Error'])==0):
			if(int(resp['Result']['rows'][0][0])==0):
				passwordHash=self.us.hash_password(password)
				statement=self.transactionGenerator.register(username=username,
				password=passwordHash,mail=mail,firstname=firstname,lastname=lastname)
				resp=self.db.make_transaction_commit(data=statement,token=t_token)
				if(login):
					self._login(username=username,password=password)
			else:
				self.dto.set_response(message='User Taken')	
		else:
			self.dto.set_response(message='System Error')
		
	def get_response(self):
		return self.dto




