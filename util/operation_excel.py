import xlrd
from xlutils.copy import copy
'''
data = xlrd.open_workbook('../dataconfig/interface.xlsx')#获取文件
tables = data.sheets()[0] #获取sheet
print(tables.nrows) #获取对应table的行数
print(tables.cell_value(2,3)) #获取单元格值
'''

class OperationExcel:
	'''
	获取excel的值
	'''
	def __init__(self, file_name=None, sheet_id=None):
		if file_name:
			self.file_name = file_name
			if sheet_id:
				self.sheet_id = sheet_id
			else:
				self.sheet_id = 0
		else:
			self.file_name = '../dataconfig/interface.xls'
			self.sheet_id = 0			

		self.data = self.get_data()


	def get_data(self):
		'''
		获取excel以及对应的sheet
		'''
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	def get_lines(self):
		'''
		获取table的行数
		'''
		return self.data.nrows

	def get_cell_value(self,row,col):
		'''
		获取单元格的值
		'''
		return self.data.cell_value(row,col)

	def write_value(self,row,col,value):
		'''
		将值写入excel
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(self.sheet_id)
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)

	def get_row_data(self,case_id):
		''' 根据case_id，返回对应case的整行内容'''
		row_num = self.get_row_num(case_id)
		return self.get_row_values(row_num)


	def get_row_num(self,case_id):
		'''根据对应case_id,导到对应案例的行号'''
		num = 0
		col_datas = self.get_col_values(0)
		for cul_data in col_datas:
			if case_id == cul_data:
				return num
			num += 1

	def get_row_values(self,row):
		'''获取对应行的内容,返回行的list'''
		return self.data.row_values(row)

	def get_col_values(self,col=0):
		'''获取对应列的内容,返回行的list'''
		return self.data.col_values(col)



if __name__ == '__main__':
	#print(OperationExcel('../dataconfig/interface.xls').get_lines())
	#print(OperationExcel().get_cell_value(2,3))
	#print(type(OperationExcel().get_row_values(2)))
	print(OperationExcel().get_row_data('login_003'))
	#OperationExcel().write_value(1,11,'pass')
	#OperationExcel().write_value(2,11,'fail')