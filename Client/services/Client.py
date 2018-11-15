import httplib, urllib
import sys
import json

#get http server ip
def makejson(key, value,action):
    root = {}
    root['action'] = action
    subarray = {}
    if len(key) != len(value):
        return None
    else:
        for i in range(len(key)):
            subarray[key[i]] = value[i]   

    root["data"] = subarray
    return json.dumps(root, ensure_ascii=False)
def connect():
    
    http_server = '127.0.0.1'
    #create a connection
    
    conn = httplib.HTTPConnection(http_server)
    return conn

def makerequest(connection,data):
    conn = connection
    headers = {"Content-type": "application/json","Accept":"application/json"}
    conn.request("POST", "/", data, headers)

    rsp = conn.getresponse()

    #print(rsp.status, rsp.reason)
    data_received = rsp.read()
    return data_received
    


