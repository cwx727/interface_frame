class global_var:
	Id = 0
	case_name = 1
	url = 2
	run =3
	request_way =4
	header = 5
	case_depend = 6
	data_depend = 7
	field_depend = 8
	data = 9
	expect = 10
	result = 11

'''
def get_id():
	return global_var.Id
'''

'''
def get_case_name():
	return global_var.case_name
'''

def get_url():
	return global_var.url

def get_run():
	return global_var.run

def get_request_way():
	return global_var.request_way

def get_header():
	return global_var.header

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

def get_field_depend():
	return global_var.field_depend

def get_data():
	return global_var.data

def get_expect():
	return global_var.expect

def get_result():
	return global_var.result

'''
def get_header_value():
	header = {
		#"Host": "www.imooc.com",
		"Connection": "keep-alive",
		"Content-Length": "329",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Origin": "https://www.imooc.com",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Referer": "https://www.imooc.com/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Cookie": "zg_did=%7B%22did%22%3A%20%2216c083665ff18a-061202ed534bde-5f1d3a17-100200-16c083666003e0%22%7D; imooc_uuid=36a87659-7cf8-4b40-9a26-eb7ab3f79c2e; imooc_isnew_ct=1563505888; UM_distinctid=16c083894202c4-0ac0311d9d782f-2d604637-4a640-16c08389421454; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1563505879,1563951747; IMCDNS=0; imooc_isnew=2; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1563953750; cvde=5d3802892f808-6; zg_f375fe2f71e542a4b890d9a620f9fb32=%7B%22sid%22%3A%201563953726982%2C%22updated%22%3A%201563953815913%2C%22info%22%3A%201563505878576%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E6%85%95%E8%AF%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E7%BB%9F%E8%AE%A1%5C%22%2C%5C%22Platform%5C%22%3A%20%5C%22web%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.imooc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201563953726982%2C%22cuid%22%3A%20%22w4cmNC8oN2Q%2C%22%7D"

	}
	return header
'''