class DatabaseStatement(object):
	def __init__():
		return
	def check_session(self,token):
		statement='SELECT COUNT(*) from session where token={0}'.format(token)
		return statement
	def login(self,user,token):
		statement='INSERT INTO SESSION (username,token)VALUES({0},{1})'.format(user,token)  
		return statement
	def get_password(self,username):
		statement='SELECT passwordHash from Person where username= %s' %username
		return statement
	def get_user(self,username):
		statement='SELECT COUNT(*) from Person where username={0}'.format(username)
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
	def register(self,username=None,password=None,firstname=None,lastname=None,email=None):
		statement="INSERT INTO PERSONS (username,passwordHash,firstName,lastName,mail) \
		VALUES({0},{1},{2},{3})".format(username,password,firstname,lastname,email)
		return statement 