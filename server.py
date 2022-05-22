import sys

class TCP:
    
	#Just populating ip_address(host) and port number of server
	def __init__(self, host='127.0.0.1'):
		self.host = host
		try:
			self.port = int(sys.argv[1])
		except Exception as e:
			self.port = 12000


if __name__ == '__main__':
    tcp_server = TCP()
    