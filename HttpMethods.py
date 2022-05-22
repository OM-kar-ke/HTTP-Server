from HttpResponse import *


class HttpMethods():   
    
	#It is called from run method of client thread class
	#It calls respective method function according to the method of http request.
	def handle_request(self, data, connection_parameters):

		# create an instance of `HttpRequest`
		request = HttpRequest(data)

		#It populates the connection parameter argument that we saw in run method of client thread class
		#It does this using the Http_Request headers that we get in client request
		lst = request.get_connection_parameters()
		connection_parameters[0][0] = lst[0][0]

		# DOUBT: Why this if condition is required?
		if (len(lst) != 1):
			connection_parameters[1][0] = lst[1][0]
			connection_parameters[1][1] = lst[1][1]


		try:
			#getattr checks if 2nd argument is an attribute or method of the current class(1st argument), if YES then assigns it to handler else throws an exception.
			handler = getattr(self, 'handle_%s' % request.method)
		except AttributeError:
			handler = self.HTTP_501_handler

		# Doubt : whether connection_parameters must be passed or not to the HTTP methods
		response = handler(request)

		return response

	def HTTP_501_handler(self, request):

		respon_line = response_line(status_code=501)
		respon_headers = response_headers()
		blank_line = b"\r\n"
		respon_body = b"<h1>501 Not Implemented</h1>"
		return b"".join([respon_line, respon_headers, blank_line, respon_body])
	
 	
	def handle_GET(self, request) :
     
		#Remove the slash from begining and end of the request URI for os.path.exists() function becos this is the function's requirement.
		filename = request.uri.strip('/') 

		if (len(filename) == 0):
			filename = server_root + "/index.html"
			filename = filename.strip('/')
   
		#if resource is present.
		if os.path.exists(filename):
			
			length_of_resource = os.path.getsize(filename)
   
			if ('If-Modified-Since' in request.req_headers_dict.keys()) :
				
				# when last modified date < If-Modified-Since date
				if (compare_dates(last_modified(request.uri), request.req_headers_dict['If-Modified-Since'])):
					respon_line = response_line(status_code=304)
					respon_headers = response_headers(request)
					respon_body = b""
     
				# when last modified date > If-Modified-Since date
				else :
					respon_line = response_line(status_code=200)
					respon_headers = response_headers(request)
					with open(filename, 'rb') as f:
						respon_body = f.read()
      
			#DOUBT : Verify if this header is present in GET or not
			elif ('If-Unmodified-Since' in request.req_headers_dict.keys()) :
				
				# when last modified date > header date
				if (not compare_dates(last_modified(request.uri), request.req_headers_dict['If-Unmodified-Since'])):
   
					respon_line = response_line(status_code=412)
					respon_headers = response_headers(request)
					respon_body = b""
     
				# when last modified date < header date
				else :
					
					respon_line = response_line(status_code=200)
					respon_headers = response_headers(request)
					with open(filename, 'rb') as f:
						respon_body = f.read()

     
			#when both If-Range and Range headers are not present
			else :
				
				respon_line = response_line(status_code=200)

				respon_headers = response_headers(request)

				with open(filename, 'rb') as f:
					respon_body = f.read()
			
   
			#Append Last-Modified Header in response.
			respon_headers = append_additional_header(respon_headers, 'Last-Modified', last_modified(filename))

			#Append Content-Type header in response.
			#find content type of requested resource
			con_type = filename.split('.')[1]
			if(con_type == 'txt'):
				content_type = 'text/plain'
			if(con_type == 'html'):
				content_type = 'text/html'
    
			respon_headers = append_additional_header(respon_headers,'Content-Type', content_type)
			

			content_length = len(respon_body)
			respon_headers = append_additional_header(respon_headers,'Content-Length', content_length)

    
     	#if resource is not present.			
		else:
			respon_line = response_line(status_code=404)
			respon_headers = response_headers(request)
			respon_body = b"<h1>404 Not Found</h1>"

		blank_line = b"\r\n"
		r = b"".join([respon_line, respon_headers, blank_line, respon_body])
		return r


