import requests
import json
import sys
sys.path.append('..')
from util.operaiton_json import OperationJson
from base.runmethod import RunMethod


class OperationHeader:
	'''判断header_method为write需write cookie进cookie.json文件，为yes，从文件中获取cookie，传入header，为no不传header'''
	def __init__(self):
		#res = json.dumps(response)
		#self.response = json.loads(res)
		self.run_method = RunMethod()
		
	'''

	def get_response_url(self,request_method,url,data):
		
		#获取登录返回的token的url
		
		res_return = self.run_method.run_main(request_method,url,data)
		res = json.dumps(res_return)
		response = json.loads(res)
		url = response['data']['url'][0]
		return url

	def get_cookie(self,request_method,url,data):
		
		#获取cookie的jar文件
		
		url = self.get_response_url(request_method,url,data)+"&callback=jQuery1910052998798084019194_1564368201817&_=1564368201819"
		cookie = requests.get(url).cookies
		return cookie

	def write_cookie(self,request_method,url,data):
		cookie = requests.utils.dict_from_cookiejar(self.get_cookie(request_method,url,data))
		op_json = OperationJson()
		op_json.write_data(cookie)
	'''

	def get_response_url(self,response):
		'''
		获取登录返回的token的url
		'''
		url = response['data']['url'][0]
		return url

	def get_cookie(self,response):
		'''
		获取cookie的jar文件
		'''
		url = self.get_response_url(response)+"&callback=jQuery1910052998798084019194_1564368201817&_=1564368201819"
		cookie = requests.get(url).cookies
		return cookie
	def write_cookie(self,response):
		'''write cookie进cookie.json文件'''
		cookie = requests.utils.dict_from_cookiejar(self.get_cookie(response))
		op_json = OperationJson()
		op_json.write_data(cookie)

	def header_main(self,header_method,request_method,url,data):
		'''判断header_method为write需write cookie进cookie.json文件，为yes，从文件中获取cookie，传入header'''
		if header_method == 'write':
			res_return = self.run_method.run_main(request_method,url,data)
			res = json.dumps(res_return)
			response = json.loads(res)
			#self.write_cookie(request_method,url,data)
			self.write_cookie(response)
			return res_return
		elif header_method == 'yes':
			cookie = OperationJson('../dataconfig/cookie.json').get_data('apsid')
			#cookies = {'apsid':cookie}
			cookies = {'Cookie':'apsid='+cookie}
			return self.run_method.run_main(request_method,url,data,cookies)
		else:
			return self.run_method.run_main(request_method,url,data)

if __name__ == '__main__':
	url = "https://www.imooc.com/passport/user/login"

	data = {"username":"17316597822",
		"password":"muke1234-",
		"verify":"",
		"referer":"https://www.imooc.com"}
	'''
	#res = json.dumps(requests.post(url,data).json())
	res = (requests.post(url,data)).json()
	print(res)

	response = OperationHeader(res)
	#print(response)
	#response.get_response_url()
	response.get_cookie()
	response.write_cookie()
	'''
	print(OperationHeader().header_main('write','POST',url,data))
