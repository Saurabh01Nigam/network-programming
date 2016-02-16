#incomplete implementation
import socket

host = 'localhost'
port = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
	client, addr = s.accept()
	print 'Got connection from ', addr
	client_msg = client.recv(1024)
	if client_msg != 'bye':
		print client_msg
		client.send(client_msg)
	client.send('Closing connection.')
	client.close()
