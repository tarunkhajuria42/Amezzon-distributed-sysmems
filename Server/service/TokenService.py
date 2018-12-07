from configparser import SafeConfigParser
import json
import uuid
import mysql.connector

DATABASE_CONFIG = 'token'
DATABASE_CONF_FILE='conf/database_config.ini'

class TokenService(object):
	
	
	def __init__(self):
		self.database_config=SafeConfigParser()
		self.database_config.read(DATABASE_CONF_FILE)
		self.config = dict(self.database_config._sections)[DATABASE_CONFIG]
		self.db=mysql.connector.connect(host=self.config['host'],port=self.config['port'],user=self.config['user'],
			passwd=self.config['password'],database=self.config['database'],auth_plugin='mysql_native_password')
		self.cursor=self.db.cursor()
		
	def set_token(self,username=None,token=None):
		statement='INSERT INTO tokens(token,username) VALUES ("{0}","{1}")'.format(token,username)
		self.cursor.execute(statement)
		self.db.commit()
		return self.cursor.rowcount

	def delete_token(self,token=None):
		statement='DELETE FROM tokens WHERE token="{0}"'.format(token)
		self.cursor.execute(statement)
		self.db.commit()
		return self.cursor.rowcount

	def retrieve_user(self,token=None):
		statement='SELECT username from tokens where token="{0}"'.format(token)
		self.cursor.execute(statement)
		users=self.cursor.fetchall()
		self.db.commit()
		if(len(users)>0):
			return users[0][0]
		else:
			return False

	def check_user_session(self,username=None):
		statement='SELECT token from tokens where username="{0}"'.format(username)
		self.cursor.execute(statement)
		users=self.cursor.fetchall()
		self.db.commit()
		if(len(users)>0):
			return True
		else:
			return False




	

			
