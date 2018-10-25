import threading
from BaseHTTPServer import BaseHTTPRequestHandler


class HttpHandlerService(BaseHTTPRequestHandler):
    def do_GET(self): # Parse the object to 
        db=DataBaseManager()
        self.send_response(200)
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

    def do_POST(self):
        print("Connection Received")
        return

    def do_PUT(self):
        return

    def do_DELETE(self):
        return
