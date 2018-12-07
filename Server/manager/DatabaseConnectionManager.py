import ssl
import httplib
import urllib
from configparser import SafeConfigParser
import traceback

DATABASE_CONFIG = 'default'
DATABASE_CONF_FILE='conf/database_config.ini'

class DatabaseConnectionManager(object):

	def __init__(self,db_type=None):
		self.database_config=SafeConfigParser()
		self.database_config.read(DATABASE_CONF_FILE)
		self.config = dict(self.database_config._sections)[DATABASE_CONFIG]
		self.conn = httplib.HTTPConnection(self.config['host'],str(self.config['port']))
		self.headers = {
					"Content-type": "application/x-www-form-urlencoded",
					"Accept": "text/plain"
 				}	

	def connect(self):
		try:
			self.conn.connect()
		except:
			traceback.print_exc()
			return False
		return True	

	def disconnect(self):
		try:
			self.conn.close()
		except:
			return False
		return True

	def request_post(self, body):
		try:
			self.conn.request('POST', '/',body)
		except:
			return False
		return True

	def request_get(self):
		try:
			self.conn.request('GET', '/')
		except:
			return False
		return True

	def get_response(self):
		try:
			res = self.conn.getresponse()
		except:
			traceback.print_exc()
			return False
		return res.read()

	def request_DELETE(self):
		return

