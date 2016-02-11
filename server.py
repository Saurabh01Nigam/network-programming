import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))

s.listen(5)

while True:
	client, addr = s.accept()
	print "Got connection from ", addr
	client.send("Thank you for connecting.")
	client.close() 