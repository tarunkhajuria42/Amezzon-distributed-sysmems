

import httplib, urllib
import sys
import json

#get http server ip
def generateLoginresponse():
    root = {}
    root['action'] = "login"
    subarray = {}
    subarray['username'] = 'tekraj'
    subarray['password'] = 'chhetri'

    root["data"] = subarray
    return json.dumps(root, ensure_ascii=False)

http_server = '127.0.0.1'
#create a connection
headers = {"Content-type": "application/json","Accept":"application/json"}
conn = httplib.HTTPConnection(http_server)

conn.request("POST", "/", generateLoginresponse(), headers)

#conn.request("GET", "/",generateLoginresponse(),headers)

    #get response from server
rsp = conn.getresponse()
    
#print server response and data
print(rsp.status, rsp.reason)
data_received = rsp.read()
print(data_received)
    
conn.close()

