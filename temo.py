import httplib
import urllib
import ssl
conn=httplib.HTTPSConnection('localhost',8080,context=ssl._create_unverified_context())
params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
          "Accept": "text/plain"}
conn.request("POST", "sd", params, headers)
