import smtplib
from email.mime.text import MIMEText

class SendEmail:
	'''发送邮件'''
	global send_user
	global email_host
	global password
	email_host = "smtp.163.com"
	send_user = 'cwx727@163.com'
	password = "a123456"
	def send_mail(self,user_list,sub,content):
		user = "cwx727" + "<"+ send_user+ ">"   #send_user发件人邮箱地址 
		message = MIMEText(content,_subtype='plain',_charset='utf-8')  #content邮件内容
		message['Subject'] =sub    #邮件主题
		message['From'] = user   #发件人
		message['To'] = ";".join(user_list)  #收件人，利用join将列表中的字段拼接
		#print(message)
		#print(type(message))
		server = smtplib.SMTP()  
		#print(server,type(server))
		server.connect(email_host)  #连接服务器email_host=smtp.163.com
		server.login(send_user,password)  #登陆邮箱的用户名和授权码，需要邮箱中设置
		server.sendmail(user,user_list,message.as_string())  #发送邮件
		server.close()  #关闭

	def send_main(self,pass_list,fail_list):
		pass_num = len(pass_list)
		fail_num = len(fail_list)
		total_num = pass_num + fail_num
		pass_result = "%.2f%%" %(float(pass_num)/float(total_num)*100)
		fail_result = "%.2f%%" %(float(fail_num)/float(total_num)*100)
		content = '本次测试通过'+str(pass_num)+'个,失败'+str(fail_num)+'个，通过率'+pass_result+',失败率'+fail_result
		sub = '接口测试报告'
		user_list=['2846634343@qq.com']
		self.send_mail(user_list,sub,content)


if __name__ == '__main__':
	#user_list=['2846634343@qq.com']
	SendEmail().send_main([1,3,5,7],[2,4])