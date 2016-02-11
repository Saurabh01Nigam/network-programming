import http.client

h = http.client.HTTPConnection("www.google.co.in")
h.request("GET", "/")
data = h.getresponse()
print (data.code)
print (data.headers)

text = data.readlines()
f = open("storage.dat", "+w")
f.write(text[3].decode("utf-8"))
f.close()
print ("Data saved to the file.")