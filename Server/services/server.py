from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import ssl

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return
    def do_POST(self):
        return	
    def do_PUT(self):
        return
    def do_DELETE(self):
        return



class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    server.socket=ssl.wrap_socket(server.socket,server_side=True, certfile='../yourpemfile.pem')
    print 'Starting server, Accepting Clients'
    server.serve_forever()