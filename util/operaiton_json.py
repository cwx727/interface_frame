import json
'''
with open('../dataconfig/login.json') as fp:
	data = json.load(fp)
print(data['login'])
'''


class OperationJson:
	'''
	读取json文件
	'''
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '../dataconfig/user.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	def read_data(self):
		'''
		读取json文件
		'''
		with open(self.file_path) as fp:
			data = json.load(fp)
		return data

	def get_data(self,id):
		'''
		获取json中某个id的值
		'''
		if id:
			return self.data[id]
		else:
			return None

	def write_data(self,data):
		with open('../dataconfig/cookie.json','w') as fp:
			fp.write(json.dumps(data))




if __name__ == '__main__':
	print(OperationJson().get_data('login'))
	OperationJson().write_data('{11:22}')

