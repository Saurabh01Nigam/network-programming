import socket

s = socket.socket()
host = 'localhost'
port = 8081
print 'Trying to connect to localhost:8080'
try:
	s.connect((host, port))
	print s.recv(1024)
except Exception, e:
	print 'Error in connection to the server.'
finally:
	s.close()

