import ssl
import httplib

SERVER_CONFIG = 'default'
CRL_PATH = 'crl/yourpemfile.pem'


class DatabaseManager(object):
    def __init__(self, ):
    	config={}
        self.conn = httplib.HTTPConnection(config['host'],config['port'])
        self.headers = {
        			"Content-type": "application/x-www-form-urlencoded",
	          		"Accept": "text/plain"
	          	}
	def connect():
		return
    def is_connected():
    	return	
    def disconnect():
    	return
    def request_post():
    	self.conn.request('')
    	if(self.is_connected()):

    	else:
    		self.connect():
   	def request_get():
   		return
   	def request_DELETE():
   		return
   	def 



        
