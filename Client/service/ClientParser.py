import urllib, json


def login(username, password):
    login_details = {}
    login_details['action'] = "login"
    data = {}
    data['username'] = username
    data['password'] = password
    login_details["data"] = data
    print json.dumps(login_details, ensure_ascii=False)

login("tekraj","chhetri")