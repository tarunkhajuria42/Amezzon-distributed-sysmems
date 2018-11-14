import ssl
import httplib
import urllib

SERVER_CONFIG = 'default'
CRL_PATH = 'crl/yourpemfile.pem'


class DatabaseManager(object):
    def __init__(self):
    	config={}
        self.conn = httplib.HTTPConnection(config['host'],config['port'])
        self.headers = {
        			"Content-type": "application/x-www-form-urlencoded",
	          		"Accept": "text/plain"
	          	}
              
  	def connect(self):
      try:
        self.conn.connect()
      except:
        return False
  		return True	

    def disconnect(self):
      try:
        self.conn.close()
      except:
        return False
    	return True 

    def request_post(self,params):
      try:
    	 self.conn.request('POST','/',params)
      except:
        return False
      return True

   	def request_get(self):
      try:
        self.conn.request('GET','/')
      except:
        return False
      return True

   	def get_response(self):
      try:
        res=self.conn.getresponse()
      except
        return False
      return res.read()

   	def request_DELETE(self):
   		return
   	



        
