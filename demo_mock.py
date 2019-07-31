import mock
from demo import RunMain

def mock_test(mock_method,request_data,url,method,response_data):
	mock_method = mock.Mock(return_value=request_data)
	res= mock_method(url,method,response_data)
	return res