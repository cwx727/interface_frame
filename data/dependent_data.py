import sys
sys.path.append('..')
from util.operation_excel import OperationExcel
from util.operaiton_json import OperationJson
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
from util.operaiton_header import OperationHeader

class DependentData:
	'''依赖数据处理'''
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()

	def get_case_line_data(self):
		'''获取excel中一行数据内容'''
		rows_data = self.opera_excel.get_row_data(self.case_id)
		return rows_data

	def run_dependent(self):
		'''
		获得值，发送request响应
		'''
		run_method = RunMethod()     
		row_num = self.opera_excel.get_row_num(self.case_id)
		request_data = self.data.get_data_from_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		#res = run_method.run_main(method,url,request_data,header)
		#res = run_method.run_main(method,url,request_data)
		res = OperationHeader().header_main(header,method,url,request_data)  
		return res

	def get_data_for_key(self,row):
		'''找到相应报文中的需要查找的依赖key值'''
		depend_data = self.data.get_depend_key(row)  #获得依赖的返回数据列
		#print('-------------depend_data',depend_data)
		response_data = self.run_dependent()    #运行获取依赖数据的行案例
		#print('-------------response_data',response_data,type(response_data))
		json_exe = parse(depend_data)       #处理depend_data
		#print('--------------json_exe',json_exe,type(json_exe))
		madle = json_exe.find(response_data)     #进行查找 
		#print('---------------madle',madle,type(madle))
		#print([math.value for math in madle])
		return [math.value for math in madle][0]   #返回查找到的结果


if __name__ == '__main__':
	#print(DependentData('login_003').get_case_line_data())
	print(DependentData('login_003').get_data_for_key(2))
