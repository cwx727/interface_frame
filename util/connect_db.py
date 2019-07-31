import MySQLdb.cursors
import json
'''
conn = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='123456',
			db='le_study',
			charset='utf8',cursorclass=MySQLdb.cursors.DictCursor
			#添加这句话，可以使返回的查询结果以字典形式返回，不添加为元祖
			)

cur = conn.cursor() #创建游标
cur.execute("select * from web_user where Name='mushishi'") #执行语句
print(cur.fetchone())  #获得查询结果单条记录
cur.execute("select * from web_user")
print(cur.fetchall())  #获得查询结果全部记录
'''
class OperationMysql:
	'''连接数据库，并传入sql查找'''
	def __init__(self):
		self.conn = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='123456',
			db='interface_frame',
			charset='utf8',
			cursorclass=MySQLdb.cursors.DictCursor
			#添加这句话，可以使返回的查询结果以字典形式返回，不添加为元祖  
			)

		self.cur = self.conn.cursor() #创建游标

	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		return json.dumps(result)

if __name__ == '__main__':
	res=OperationMysql().search_one("select * from web_user where Name='mushishi'")
	print(res)
	print(type(res))