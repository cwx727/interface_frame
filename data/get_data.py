import sys
sys.path.append('..')
from util.operation_excel import OperationExcel
from util.operaiton_json import OperationJson
import data.data_config
from util.connect_db import OperationMysql

class GetData:
	'''获取excel的数据值'''
	def __init__(self):
		self.oper_excel = OperationExcel()

	def get_case_lines(self):
		'''
		获取excel行数，即案例个数
		'''
		return self.oper_excel.get_lines()

	def get_is_run(self,row):
		'''
		获取是否允许
		'''
		flag = None
		col = data.data_config.get_run()
		run_model = self.oper_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	def is_header(self,row):
		'''
		获取是否有header
		'''
		col = data.data_config.get_header()
		header = self.oper_excel.get_cell_value(row,col)

		'''
		if header == 'yes' :
			return data.data_config.get_header_value()
		else:
			return None
		'''
		if header == 'yes' or 'write' :
			return header
		else:
			return None


	def get_request_method(self,row):
		'''
		获取请求方式
		'''
		col = data.data_config.get_request_way()
		request_method = self.oper_excel.get_cell_value(row,col)
		return request_method

	def get_request_url(self,row):
		col = data.data_config.get_url()
		url = self.oper_excel.get_cell_value(row,col)
		return url

	def get_request_data(self,row):
		col = data.data_config.get_data()
		request_data = self.oper_excel.get_cell_value(row,col)
		if request_data == '':
			return None
		else:
			return request_data

	def get_data_from_json(self,row):
		data_from_json = self.get_request_data(row)
		request_data = OperationJson().get_data(data_from_json)
		return request_data

	def get_expect_data(self,row):
		col = data.data_config.get_expect()
		expect_data = self.oper_excel.get_cell_value(row,col)
		if expect_data == '':
			return None
		else:
			return expect_data

	def get_expect_data_for_mysql(self,row):
		sql = self.get_expect_data(row)
		if sql[:6] == 'select':
			res = OperationMysql().search_one(sql)
			expect_type = 'sql'
		else:
			res = sql
			expect_type = 'notsql'
		return res,expect_type



	def write_result(self,row,value):
		col = data.data_config.get_result()
		self.oper_excel.write_value(row,col,value)

	def get_depend_key(self,row):
		col = data.data_config.get_data_depend()
		depend_key = self.oper_excel.get_cell_value(row,col)
		if depend_key == '':
			return None
		else:
			return depend_key

	def get_field_depend_value(self,row):
		col = data.data_config.get_field_depend()
		field_depend_value = self.oper_excel.get_cell_value(row,col)
		if field_depend_value == '':
			return None
		else:
			return field_depend_value

	def get_case_depend_value(self,row):
		col = data.data_config.get_case_depend()
		get_case_depend_value = self.oper_excel.get_cell_value(row,col)
		if get_case_depend_value == '':
			return None
		else:
			return get_case_depend_value

if __name__ == '__main__':
	getdata = GetData()
	print('lines',getdata.get_case_lines())

	print('is_run',getdata.get_is_run(1))
	print('header',getdata.is_header(1))
	print('request_method',getdata.get_request_method(1))
	print('request_url',getdata.get_request_url(1))
	print('request_data',getdata.get_data_from_json(1))
	print('request_data',type(getdata.get_data_from_json(1)))
	print('expect_data',getdata.get_expect_data(1))
	print('depend_key',getdata.get_depend_key(1))
	print('depend_key',getdata.get_field_depend_value(1))

	print('sql',getdata.get_expect_data_for_mysql(3),type(getdata.get_expect_data_for_mysql(3)))



