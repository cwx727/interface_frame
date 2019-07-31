import requests
import json

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class RunMain():
	'''
	def __init__(self,url,method,data=None):
		self.res = self.run_main(url,method,data=None)
	'''

	def send_get(self,url,data=None):
		res = requests.get(url,data=data,verify=False).json()
		#return json.dumps(res,indent=True,sort_keys=True)
		return res

	def send_post(self,url,data=None):
		res = requests.post(url,data=data,verify=False).json()
		#return json.dumps(res,indent=True,sort_keys=True)
		return res

	def run_main(self,url,method,data=None):
		if method == 'GET':
			return self.send_get(url,data)
		elif method == 'POST':
			return self.send_post(url,data)


if __name__ == '__main__':
	url1 = 'https://m.imooc.com/wap/api/course/loadCourseList?marking=all&course_type=0&easy_type=&order=2&pageIndex=1&flag=&ex_learned=0'
	data1 = {'marking':'all',
			'course_type':0,
			'easy_type':'',	
			'order':2,
			'pageIndex':1,
			'flag':'',	
			'ex_learned':0,}
	print('-----post-----\n',RunMain().run_main(url1,'POST',data1))
	print(type(RunMain().run_main(url1,'POST',data1)))
	url2 = 'https://m.imooc.com/api/search/searchword'
	print('-----get-----\n',RunMain().run_main(url2,'GET'))

