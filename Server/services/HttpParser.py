from http_parser.parser import HttpParser

class http_parser:
	def __init__:
		self.parser = HttpParser()

	def get_header():
		return self.parser.get_headers()

	def is_header_complete():
		return self.parser.is_header_complete()

	def is_body_complete():
		return self.parser.is_body_complete()

	def is_patial_body():
		return self.parser.is_patial_body()

	def recv_body():
		return self.parser.recv_body()

	def parse(data,size):
		self.parser.execute(data,size)
		return True
	def parse_request(data):
		if()

