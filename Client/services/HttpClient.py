from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

concurrent = 10


def Start():
    while True:
        url = q.get()
        resp, url = getStatus(url)
        printResult(resp, url)
        q.task_done()

def getStatus(connect_address):
    try:
        conn = httplib.HTTPSConnection(connect_address)
        print(url,"trying to connect")
        conn.request("GET", '/')
        response = conn.getresponse()
        return response, connect_address
    except:
        return "error", connect_address

def printResult(response, address):
    if response.status == 200:
        print "Response from ",address
        print "################################################################################"                
        print response.read()
        print "############################################## END ##############################"
    else:
        print "Bad response from server"

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=Start)
    t.daemon = True
    t.start()
try:
    urls = ["172.17.161.83:8080","172.17.161.83:8080"]
    for url in urls:
        print url
        q.put(url)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
