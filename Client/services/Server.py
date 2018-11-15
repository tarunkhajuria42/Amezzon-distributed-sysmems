# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import cgi
from urlparse import *

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
 
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        # refuse to receive non-json content
        
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
        length = int(self.headers.getheader('content-length'))
        
        message = json.loads(self.rfile.read(length))
        message['Request']='GET'
        
        self._set_headers()
        self.wfile.write(json.dumps(message))
        
    # POST echoes the message adding a JSON field
    
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        print(pdict)
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
    
        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        #message = message.decode()
        message = json.loads(self.rfile.read(length))
        
        
        
        # add a property to the object, just to mess with data
        #if(message['username'] == 'tekraj'):
        #    message['received'] = 'ok'
        #message['Request']='POST'
        #dummy product data
        product = {"laptop":{"price":555,"brand":"Apple","launchYear":"1/1/2018","category":"electronic","description":"MacBook Pro elevates the notebook to a whole new level of performance and portability. Wherever your ideas take you, you’ll get there faster than ever with high‑performance processors and memory, advanced graphics, blazing‑fast storage, and more."},
                   "jacket":{"price":55,"brand":"Nike","launchYear":"1/1/2016","category":"clothing"},
                   "headset":{"price":299.95,"brand":"Apple","launchYear":"1/11/2018","category":"electronic","description":"With up to 40 hours\
                        of battery life, Beats Solo3 Wireless is your perfect everyday headphone Premium playback and fine-tuned acoustics maximize \
                        clarity, breadth, and balance Adjustable fit with comfort-cushioned ear cups made for everyday use. 5 minutes of charging gives \
                        you 3 hours of playback when battery is lowTake calls, control your music and activate Siri with the multifunction on-ear controls \
                        Comes with Beats Solo3 Wireless headphones, carrying case, 3.5mm RemoteTalk cable, Universal USB charging cable \
                        (USB-A to USB Micro-B), Quick Start Guide and Warranty Card"},
                   "mobile":{"price":100,"brand":"Apple","launchYear":"1/18/2015","category":"electronic","description":"A blend of the technology and design"},
                   "shoe":{"price":87,"brand":"Nike","launchYear":"10/19/2018","category":"sports","description":"A perfect blend of years of work put into your feet, designed for footballers. Just grab it and feel the difference in playing"},
                   }
        # send the message back
        respmessage = {}
        #print (message["action"])
        #testing login response
        if message["action"] == "login":            
            if message['data']['username'] == 'tekraj':
                respmessage['username'] = 'tekraj'
                respmessage['doj'] = '11/2/2018'
                respmessage['status'] = 'active'

            print(message['data']['username'])

        #to test product request data only single product by key
        #print message
        if message["action"] == "product":
            
            if len(message['data']) == 1:
                respmessage["action"] = "product"
                respmessage[message['data']['product']] = product[message['data']['product']]
            elif len(message['data']) > 1:
                results = []
                
                #simple hardcoded for testing
                if message['data']['product'] in product.keys():
                    print "IN",message['data']['brand'],message['data']['product']
                    checkproduct = product[message['data']['product']]
                    brand  = checkproduct['brand'].lower()
                    #print brand
                    if message['data']['brand'] == brand:
                        respmessage[message['data']['product']] = checkproduct
                       # print product[message['data']['product']]
                else:
                    respmessage["error"] = "No criteria match"
            else:
                respmessage["error"] = "Error match"
                
                


            #print message['data']['product']
            

        
       
            
    
        self._set_headers()
        self.wfile.write(json.dumps(respmessage))
        
def run(server_class=HTTPServer, handler_class=Server, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print 'Starting httpd on port %d...' % port
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
