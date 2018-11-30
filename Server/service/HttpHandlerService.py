from BaseHTTPServer import BaseHTTPRequestHandler

from dto.ErrorMessage import ErrorMessageList
from dto.client.LoginDto import LoginDto
from parser.ClientRequestParser import ClientRequestParser
from model.MainModel import MainModel


class HttpHandlerService(BaseHTTPRequestHandler):
    def do_GET(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.response())
        self.end_headers()
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.response())
        self.end_headers()
        return

    def do_PUT(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.response())
        self.end_headers()

        return

    def do_DELETE(self):
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        model=MainModel(request=body)
        self.wfile.write(model.response())
        self.end_headers()

        return
