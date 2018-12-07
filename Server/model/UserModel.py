from service.UserService import UserService
import uuid

class UserModel:
	def __init__(self,transactionGen,dbConnection,dto,tk):
		self.dto=dto
		self.transactionGenerator=transactionGen
		self.us=UserService()
		self.db=dbConnection
		self.tk=tk
		if(dto.action=='login'):
			response=self._login(username=dto.username,password=dto.password)
		elif(dto.action=='logout'):
			response=self._logout(token=dto.token)
		elif(dto.action=='user_information'):
			reponse=self._get_details(token=dto.token)
		elif(dto.action=='user'):
			response=self._set_details(token=dto.token,firstname=dto.first_name,
				lastname=dto.last_name,mail=dto.mail,password=dto.password)
		elif(dto.action=='registration'):
			reponse=self._register(username=dto.username,password=dto.password,
				mail=dto.mail,firstname=dto.firstname,lastname=dto.lastname,login=dto.login)
		return

	def _login(self,username=None,password=None):
		t_token=self.db.init_transaction()	
		statement=self.transactionGenerator.get_password(username=username)
		resp=self.db.make_transaction_commit(data=statement,token=t_token)
		if(len(resp['Result']['rows'][0])==0):
			self.dto.set_response(message='wrong_input')
			return
		else:
			stored_hash=resp['Result']['rows'][0][0]
		if(self.us.check_password(password,stored_hash)):
			token=str(uuid.uuid1())
			resp=self.tk.set_token(username=username,token=token)
			if(resp>0):
				self.dto.set_response(token=token)
			else:
				self.dto.set_response(message='system_error',message_connection='login')
		else:
			self.dto.set_response(message='wrong_input')

	def _get_session(self,token=None):
		resp=self.tk.retrieve_user(token=token)
		return resp

	def _logout(self,token=None):
		uname=self._get_session(token)
		if(uname):
			resp=tk.delete_token(token)
			if(resp>0):
				self.dto.set_response()	
			else:
				return False

	def _get_details(self,token=None):
		uname=self._get_session(token)
		if(uname):
			statement=self.transactionGenerator.get_user_details(username=uname)
			self.db.init_transaction()
			resp=self.db.make_transaction_commit(statement)
			if(len(resp['Error'])==0):
				id_num=int(resp['Result']['rows'][0][0])
				firstname=resp['Result']['rows'][0][1]
				lastname=resp['Result']['rows'][0][2]
				mail=resp['Result']['rows'][0][3]
				self.dto.set_response(first_name=firstname,
							last_name=lastname,mail=mail,username=uname,id_number=id_num)
			else:
				self.dto.set_response(message='system_error',message_connection='user_information')
				return True
		return result

	def _set_details(self,token=None,mail=None,firstname=None,lastname=None,):
		uname=self._get_session(token)
		if(uname):
			passwordHash=self.us.hash_password(password)
			statement=statement=self.transactionGenerator.set_details(username=uname,password=passwordHash,mail=mail,
			firstname=firstname,lastname=lastname)
			db_token=self.db.init_transaction()
			resp=self.db.make_transaction_commit(data=statement,token=db_token)
			if(len(resp['Error']) == 0):
				self.dto.set_response()
			else:
				self.dto.set_response(message='system_error',message_connection='user')
		else:
			self.dto.set_response(message='session_expired',message_connection='session')

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
					self.dto.set_response()
			else:
				self.dto.set_response(message='User Taken')	
		else:
			self.dto.set_response(message='System Error')
		
	def get_response(self):
		return self.dto




