import unittest


class Testmethod(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print('setUpClass')
	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		print('setUp')

	def tearDown(self):
		print('tearDown')

	def test_01(self):
		print('test_01')

	def test_02(self):
		print('test_02')

if __name__ == '__main__':
	unittest.main()