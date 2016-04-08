#client code for simplest chat applcation
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 4000

s.connect((host, port))

while True:
	inp = raw_input()
	s.send(inp)
	print s.recv(1024)

s.close()