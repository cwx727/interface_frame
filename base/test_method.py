import unittest
from demo import RunMain
import HtmlTestRunner
import mock
from demo_mock import mock_test

class Testmethod(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print('setUpClass')
	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		self.run = RunMain()

	def tearDown(self):
		print('tearDown')

	def test_01(self):
		url1 = 'https://m.imooc.com/wap/api/course/loadCourseList?marking=all&course_type=0&easy_type=&order=2&pageIndex=1&flag=&ex_learned=0'
		data1 = {'marking':'all',
				'course_type':0,
				'easy_type':'',	
				'order':2,
				'pageIndex':1,
				'flag':'',	
				'ex_learned':0,}

		res=self.run.run_main(url1,'POST',data1)
		
		self.assertEqual(res['code'],200,'测试成功')
		globals()['user_id']='1203818'

	#@unittest.skip('test_02')  #跳过该案例
	def test_02(self):
		print(user_id)
		url2 = 'https://m.imooc.com/api/search/searchword'
		res=self.run.run_main(url2,'GET')
		
		self.assertEqual(res['errorCode'],1000,'测试成功')
		#self.assertNotEqual(res['errorCode'],1001,'测试成功')

	#mock方法
	def test_03(self):
		url1 = 'https://m.imooc.com/wap/api/course/loadCourseList?marking=all&course_type=0&easy_type=&order=2&pageIndex=1&flag=&ex_learned=0'
		data1 = {'marking':'all',
				'course_type':0,
				'easy_type':'',	
				'order':2,
				'pageIndex':1,
				'flag':'',	
				'ex_learned':0,}

		res = mock_test(self.run.run_main,data1,url1,'POST',data1)
		#self.run.run_main = mock.Mock(return_value=data1)
		#res=self.run.run_main(url1,'POST',data1)
		print(res)
		
		self.assertEqual(res['ex_learned'],0,'测试成功')


if __name__ == '__main__':
	#unittest.main()

	suite = unittest.TestSuite()
	suite.addTest(Testmethod('test_01'))
	suite.addTest(Testmethod('test_02'))
	suite.addTest(Testmethod('test_03'))
	unittest.TextTestRunner().run(suite)
	#HtmlTestRunner.HTMLTestRunner(output='../report/').run(suite)
