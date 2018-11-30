from manager.DatabaseConnectionManager import DatabaseConnectionManager
import json
class DatabaseService(object):
	def __init__(self,service_manager):
		self.conn=DatabaseConnectionManager()
		self.conn.connect()

	def init_transaction(self):
		req={}
		req['action']="database statement"
		req['data']={}
		str_request=json.loads(req)


	def make_transaction(self,data):
		req={}
		req['action']="database statement"
		req['data']=data
		str_request=json.loads(req)

	



	

			
