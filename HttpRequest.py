#This class contains all imp attributes([method, uri, http_version], [request_headers_dict], [request_msg]) from http request
#It also has a parser method to parse the http request msg and populate the above attribute feilds.



#Flow of data(raw http reuqest)
# 1.recieved from connection socket					(In client thread class run method)
# 2.passed as a parameter to handle_request			(In client thread class run method)
# 3.in handle request HttpRequest class object is created in which this "data" is passed to its constructor
# 4.Data is then parsed into above fields, where paraser function is called in constructor itself.



# Class to Parse Request recieved from clients
class HttpRequest:
	def __init__(self, data):
		self.method = None
		self.uri = ""
		self.http_version = "1.1"

		# collected the message body and store them in a list
		self.request_msg = []
	
		# created a dictonary for headers to eaisly access the headers and values for the headers 
		self.req_headers_dict = {}
	 
		# call self.parse() method to parse the request data
		self.parse(data)





