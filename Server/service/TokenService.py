from manager.DatabaseConnectionManager import DatabaseConnectionManager
import json
import uuid

class TokenService(object):
	def __init__(self):
		self.conn=DatabaseConnectionManager(db_type='token')
		self.conn.connect()
		
	def make_transaction(self,data=None):
		self.conn.request_post(str_request)
		resp=self.conn.get_response()
		resp=json.loads(resp)
		return resp



	

			
