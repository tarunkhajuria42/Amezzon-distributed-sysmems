import ssl
import httplib
import urllib

DATABASE_CONFIG = 'default'
DATABASE_CONF_FILE='conf/database_config.ini'

class DatabaseManager(object):

    def __init__(self,service_manager):
      self.service_manager=service_manager
      self.database_config=SafeConfigParser()
      self.database_config.read(DATABASE_CONF_FILE)
      self.config = dict(database_config._sections)[DATABASE_CONFIG]
      self.conn = httplib.HTTPConnection(self.config['host'],self.config['port'])
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
   	



        
