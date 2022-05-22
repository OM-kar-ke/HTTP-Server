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
	

