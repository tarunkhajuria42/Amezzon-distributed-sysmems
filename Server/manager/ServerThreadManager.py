from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn


class ServerThreadManager(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
