#incomplete implementation
import socket

host = 'localhost'
port = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:	
	inp = raw_input()
	s.send(inp)
	print s.recv(1024)
