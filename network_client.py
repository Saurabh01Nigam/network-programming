import socket

host = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#STREAM-TCP, DGRAM-UDP
#AF_INET-Internet Family
addr = (host, 8080) #tuple
s.connect(addr)

try:
	message = b"Message sent from client to server.\n" #sending array of bytes
	s.sendall(message)
	print s.recv(1024)
except socket.errno as e:
	print("Socket error- ", e)
finally:
	s.close()

