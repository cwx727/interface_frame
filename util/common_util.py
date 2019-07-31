import json

class CommondUtil:
	'''对比预期结果和实际结果是否一致'''
	def is_contain(self, str_one, str_two):
		'''判断str_one是否在str_two中'''
		flag = False
		if str(str_one) in str(str_two):
			flag = True
		return flag

	def is_equal_dict(self, dict_one, dict_two):
		if isinstance(dict_one,str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two,str):
			dict_two = json.loads(dict_two)
		#print(dict_one,dict_two)

		for i in dict_one:
			if i not in dict_two.keys():
				return False
			else:
				#print('dict_two.keys()',dict_two.keys())
				flag = self.is_contain(dict_one[i],dict_two[i])
				#print('flag',flag)
				if flag==False:
					return flag
		return flag
		
	def is_equal(self,equal_one,equal_two,equal_one_type):
		'''判断预期结果是sql还是str，如果是sql，调用is_equal_dicta(),不是，调用is_contain()'''
		if equal_one_type == 'sql':
			return self.is_equal_dict(equal_one,equal_two)
		else:
			return self.is_contain(equal_one,equal_two)




if __name__ == '__main__':
	str1 = "'data': {'remind': 0}"
	str2 = {'status': 1, 'data': {'search': [{'name': 'Java入门', 'links': 'http://class.imooc.com/sc/64'}, {'name': '前端入门', 'links': 'http://class.imooc.com/sc/53'}], 'history': [], 'hotword': [{'id': '7', 'name': 'java'}, {'id': '1', 'name': 'python'}, {'id': '40', 'name': 'vue'}, {'id': '28', 'name': 'spring'}, {'id': '116', 'name': '小程序'}, {'id': '198', 'name': 'react'}, {'id': '87', 'name': 'linux'}, {'id': '165', 'name': 'mysql'}, {'id': '46', 'name': 'docker'}]}, 'errorCode': 1000, 'errorDesc': '成功', 'timestamp': 1563939261041}
	#print(CommondUtil().is_contain(str1,str2))
	dict1 =  '{"Name": "mushishi", "age": 18}'
	dict2 = {'result': 0, 'data': {'remind': 0}, 'msg': '成功'}
	print(CommondUtil().is_equal(str1,dict2,'notsql'))
	#print(CommondUtil().is_equal_dict(str1,dict2))