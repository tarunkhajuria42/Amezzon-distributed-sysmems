import httplib

class HttpClientService:
    def __init__(self, url="127.0.0.1", sendrequest=""):
        self.url = url
        self.sendrequest = self

    def connect(self):
        try:
            connect = httplib.HTTPSConnection(self.url)
            return connect
        except:
            print "Connection Error"


    def sendRequest(self,connection, requests = "/"):
        connection.request("GET", requests)
        return connection.getresponse()




if __name__ == '__main__':
    client = HttpClientService("www.google.com")
    connection = client.connect()
    if connection:
         resp = client.sendRequest(connection,"/")
         if resp.status == 200:
             print resp.read()
         else:
             print "bad response from server"



