import requests
import json
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
'''

url = 'https://www.imooc.com/apiw/uidaes?uid=7989954'
#url = 'http://www.baidu.com'
#data = {'uid': '7989954'}

res = requests.get(url,data=None).json()
print(json.dumps(res,indent=2,sort_keys=True))