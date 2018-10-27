import urllib, json

class LoginService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def generateLoginresponse(self):
        root = {}
        root['action'] = "login"
        subarray = {}
        subarray['username'] = self.username
        subarray['password'] = self.password
        root["data"] = subarray
        return json.dumps(root, ensure_ascii=False)


    def loginRequest(self):
        getloginResponse = self.generateLoginresponse()
        print (getloginResponse)




if __name__ == '__main__':
    clients = LoginService("tekraj", "chhetri")
    clients.loginRequest()
    clients.generateLoginresponse()