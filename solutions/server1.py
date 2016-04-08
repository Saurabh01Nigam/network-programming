import datetime
import socket

def currentdatetime():
	d = datetime.datetime.now()
	return str(d)

host = 'localhost'
port = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
for i in range(5):
	client, addr = s.accept()
	print 'Got connection from ', addr
	client.send(str(currentdatetime()))
	client.close()
print 'Closing server'
s.close()