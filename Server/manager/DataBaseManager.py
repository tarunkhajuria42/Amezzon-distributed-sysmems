import ssl
import httplib

SERVER_CONFIG = 'default'
CRL_PATH = 'crl/yourpemfile.pem'


class DatabaseManager(object):
    def __init__(self, ):

        conn = httplib.HTTPConnection("bugs.python.org")
        headers = {
        			"Content-type": "application/x-www-form-urlencoded",
	          		"Accept": "text/plain"
	          	}

    def request(self):
        print 'Starting server, Accepting Clients'
        self.server.serve_forever()
