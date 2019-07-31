import sys
sys.path.append('..')
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommondUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail
from util.operaiton_header import OperationHeader
from util.operaiton_json import OperationJson


class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommondUtil()
		self.email = SendEmail()

	def go_on_run(self):
		'''主运行程序'''
		res = None
		pass_count = []
		fail_count = []
		row_count = self.data.get_case_lines()
		for i in range(1,row_count):
			url = self.data.get_request_url(i)
			method = self.data.get_request_method(i)
			data = self.data.get_data_from_json(i)
			header = self.data.is_header(i)
			is_run = self.data.get_is_run(i)
			#expect_result = self.data.get_expect_data(i)
			expect_result,expect_result_type = self.data.get_expect_data_for_mysql(i)
			#expect_result_type = self.data.get_expect_data_for_mysql(i)[1]
			#print('-------expect_result',expect_result)
			#print('-------expect_result_type',expect_result_type)
			depend_case = self.data.get_field_depend_value(i)
			if is_run:
				if depend_case:
					#print('1111---------depend_case',depend_case)
					case_id = self.data.get_case_depend_value(i)  #允许数据依赖逻辑
					#print('1111---------case_id',case_id)
					value = DependentData(case_id).get_data_for_key(i)   
					#print('1111------------value',value)
					#判断是否为post请求，如果是，将data中的值刷新，如果为get，将依赖值，赋值给url
					if method == 'POST':
						data[depend_case] = value
					else:
						url = url + '?' + depend_case + '=' + value
						#print('-------------url', url)
				#print('-------data',data)
				'''
				if header == 'write':
					res = self.run_method.run_main(method,url,data)
					OperationHeader(res).write_cookie()
				elif header == 'yes':
					cookie = OperationJson('../dataconfig/cookie.json').get_data('apsid')
					cookies = {'apsid':cookie}
					res = self.run_method.run_main(method,url,data,cookies)
				else:
					res = self.run_method.run_main(method,url,data)
				'''
				#res = OperationHeader().header_main(header,method,url,data)
				res = OperationHeader().header_main(header,method,url,data)   #head判断和处理

				#print('---------',expect_result)
				#print('----res',res,type(res))
				#if self.com_util.is_contain(expect_result,res):#字符串判断
				if self.com_util.is_equal(expect_result,res,expect_result_type):   #测试结果写入excel
					self.data.write_result(i,'pass')
					pass_count.append(i)
				else:
					self.data.write_result(i,str(res))
					fail_count.append(i)
		self.email.send_main(pass_count,fail_count)   #发送邮件

if __name__ == '__main__':
	RunTest().go_on_run()