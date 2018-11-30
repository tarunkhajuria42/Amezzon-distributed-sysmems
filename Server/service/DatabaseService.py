from manager.DatabaseConnectionManager import DatabaseConnectionManager
import json
import uuid
class DatabaseService(object):
	def __init__(self):
		self.conn=DatabaseConnectionManager()
		self.conn.connect()

	def init_transaction(self):
		req={}
		req['action']="database statement"
		req['data']={}
		str_request=json.dumps(req)
		self.conn.request_post(str_request)
		return self.conn.get_response()

	def make_transaction(self,data):
		req={}
		req['action']="database statement"
		statements={}
		t_id=uuid.uuid1()
		s_id=uuid.uuid1()
		statement={}
		statement['statement_id']=s_id
		statement['statement']=data
		statements['statement_list']=[statement]
		statements['transaction_token']=t_id
		req['data']=statement
		str_request=json.dumps(req)
		self.conn.request_post(str_request)
		resp=self.conn.get_response()
		resp=json.loads(resp)
		res={}
		res['Result']=resp['data']['result_list'][0]['result_message']
		res['Error']=resp['data']['Error_messages'][0]['message']
		return resp['data']['result_list']['result_message']


	



	

			
