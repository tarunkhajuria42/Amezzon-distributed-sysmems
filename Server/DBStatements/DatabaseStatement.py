class DatabaseStatement(object):
	def __init__(self):
		return
	def check_session(self,token):
		statement='SELECT COUNT(*) from session where token={0}'.format(token)
		return statement
	def login(self,user,token):
		statement='INSERT INTO SESSION (username,token)VALUES({0},{1})'.format(user,token)  
		return statement
	def get_password(self,username):
		statement='SELECT person_passwordhash from person where person_username= "{0}"'.format(username)
		return statement
	def get_user(self,username):
		statement='SELECT COUNT(*) from person where person_username="{0}"'.format(username)
		return statement
	def set_user(self):
		return
	def transaction(self):
		return
	def transaction_record(self):
		return
	def get_products(self):
		return
	def set_user(self):
		return
	def register(self,username=None,password=None,firstname=None,lastname=None,mail=None):
		statement='INSERT INTO person(person_username,person_passwordhash,person_firstName,person_lastName,person_mail) \
		VALUES("{0}","{1}","{2}","{3}","{4}")'.format(username,password,firstname,lastname,mail)
		return statement 
	def commit(self):
		statement="commit"