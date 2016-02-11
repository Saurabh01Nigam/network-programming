import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 8080)
s.bind(addr)

s.listen(5)
while True:
	client, client_addr = s.accept()
	print client, client_addr #observe the output
	data = client.recv(1024)
	if data:
		print ("Client address- ", client_addr)
		print data
		client.send("Thank you for connecting.")
		f = open("storage.dat", 'w')
		f.write(data.decode("utf-8"))
		f.close()
s.close()