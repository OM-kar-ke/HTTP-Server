import socket
import sys
from threading import Thread
import threading

class TCP:
    
	#Just populating ip_address(host) and port number of server
	def __init__(self, host='127.0.0.1'):
		self.host = host
		try:
			self.port = int(sys.argv[1])
		except Exception as e:
			self.port = int(config['TCP']['port'])

	#server starts on calling the start_tcp function
	def start_tcp(self):
     
		# create a TCP socket object for listening to TCP requests
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        		
		
		# bind the socket object to the address and port
		s.bind((self.host, self.port))	        
		
		# start listening for connection requests
		s.listen(int(config['TCP']['queuesize']))

		print("Server is listening at : ", s.getsockname(),'\n')

		# List which stores ClientThreads objects
		threads = []

		# MAX TCP connections that we can have working simultaneously
		max_simul_connec = int(config['TCP']['max_conn'])

		# Server is listening
		# It is waiting on s.accept() till any client makes an http request to it
		# When some client makes an request, it creates an connection socket for it
		# Then this http request is processed on new thread
		while True:
      
			# Creates a new connection socket and accept new connection
			conn, (ip, port) = s.accept()
			print("\n\nConnected by a client with address : ", ip," ",port)

			if(threading.active_count()<=max_simul_connec):
				#Creating a new client thread object 
				newthread = ClientThread(conn, ip, port)

				#Whenever we use multithreading in python we must have a run method in the class(which is inheriting Thread class) to do multi-threading.
				# The class that inherits Thread class must have a run method in it , which will be executed as a thread function when an instance of that class(child of thread class) calls .start method.

				newthread.start()
				threads.append(newthread)
			else:
				print("\nMaximum Connections reached\n")

class ClientThread(Thread):
    pass

#Instances of this class are created every time server receives a connection request.
class ClientThread(Thread):

	def __init__(self, conn, ip, port): 
		Thread.__init__(self)
		self.conn = conn 
		self.ip = ip 
		self.port = port 
		print ("New server socket thread started for " + ip + ":" + str(port), '\n')
 

if __name__ == '__main__':
    tcp_server = TCP()
    tcp_server.start_tcp()