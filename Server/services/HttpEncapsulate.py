import urllib
class http_encap:
	def __init__:

	def get_version():
		return "HTTP 1.1/"

	def get_response(code):
		http_response_type={ 200 : "OK"  # needs to go globally
			   400 : "Bad Request"
			   403 : "Forbidden"
			   404 : "Not found"
		}	
		return str(code)+' '+ type(code)

	def url_encode(data):
		return urllib.urlencode(data)

	def generate_request(request,head,body):
		return request +'\n'+head +'\n'+ body

	def gererate_response(response,head,body):
		return response +'\n'+head +'\n'+ body