from BaseHTTPServer import BaseHTTPRequestHandler

from dto.ErrorMessage import ErrorMessageList
from dto.client.LoginDto import LoginDto
from parser.ClientRequestParser import ClientRequestParser
from model.MainModel import MainModel


class HttpHandlerService(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.get_response())
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.get_response())
        self.end_headers()
        print(model.get_response())
        return

    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.get_response())
        self.end_headers()
        return

    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.get_response())
        self.end_headers()

        return
