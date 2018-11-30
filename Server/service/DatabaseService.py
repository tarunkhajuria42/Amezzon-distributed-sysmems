from manager.DatabaseConnectionManager import DatabaseConnectionManager
import json
import uuid
class DatabaseService(object):
	def __init__(self):
		self.conn=DatabaseConnectionManager()
		self.conn.connect()

	def init_transaction(self):
		req={}
		req['action']="initialize transaction"
		req['data']={}
		str_request=json.dumps(req)
		self.conn.request_post(str_request)
		resp=self.conn.get_response()
		resp=json.loads(resp)
		if('data' in resp.keys()):
			data=resp['data']
			if('token' in data.keys()):
				return data['token']
			else:
				return False
		else:
			return False
		

	def make_transaction(self,data=None,token=None):
		req={}
		req['action']="database statement"
		statements={}
		s_id=str(uuid.uuid1())
		statement={}
		statement['statement_id']=s_id
		statement['statement']=data
		statements['statement_list']=[statement]
		statements['transaction_token']=token
		req['data']=statements
		str_request=json.dumps(req)
		print(str_request)
		self.conn.request_post(str_request)
		resp=self.conn.get_response()
		resp=json.loads(resp)
		res={}
		res['Result']=resp['data']['result_list'][0]['result_message']
		res['Error']=resp['data']['Error_messages'][0]['message']
		return resp['data']['result_list']['result_message']


	



	

			
