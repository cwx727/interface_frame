import requests
import json
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
'''

url = 'https://www.imooc.com/passport/user/login'
data = {"username":"17316597822",
	"password":"muke1234-",
	"verify":"",
	"referer":"https://www.imooc.com"}

#res = requests.post(url,data=data,verify=False)
res = requests.post(url,data=data).json()
print(type(res))

print(json.dumps(res,indent=True,sort_keys=True))