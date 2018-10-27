from BaseHTTPServer import BaseHTTPRequestHandler

from dto.ErrorMessage import ErrorMessageList
from dto.client.LoginDto import LoginDto
from parser.ClientRequestParser import ClientRequestParser


class HttpHandlerService(BaseHTTPRequestHandler):
    def do_GET(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        parser = ClientRequestParser(json_string=body, method='GET')
        request_dto = parser.get_body()

        print request_dto.toJSON()

        self.send_response(200)
        self.end_headers()

        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        parser = ClientRequestParser(json_string=body, method='POST')
        request_dto = parser.get_body()

        print request_dto.get_action()

        self.send_response(200)
        self.end_headers()

        response_dto = LoginDto.PostResponse(
            token='TEST',
            error_messages=ErrorMessageList()
        )
        self.wfile.write(response_dto.toJSON())
        return

    def do_PUT(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        parser = ClientRequestParser(json_string=body, method='PUT')
        request_dto = parser.get_body()

        print request_dto.toJSON()

        self.send_response(200)
        self.end_headers()

        return

    def do_DELETE(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        parser = ClientRequestParser(json_string=body, method='DELETE')

        request_dto = parser.get_body()
        self.send_response(200)
        self.end_headers()

        return
