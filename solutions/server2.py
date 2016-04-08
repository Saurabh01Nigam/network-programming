# simplest chat server
import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
	print 'Waiting for Connections.'
	client, addr = s.accept()
	print 'Got connection from ', addr

	while True:
		print client.recv(1024)
		server_inp = raw_input() 	
		client.send(server_inp)
		

	client.close()

