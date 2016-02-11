import pcapy

devices = pcapy.findalldevs()
print devices

#output - ['eth0', 'any', 'lo', 'wlan0', 'bluetooth-monitor', 'nflog', 'nfqueue', 'usbmon1', 'usbmon2', 'usbmon3', 'usbmon4']

cap = pcapy.open_live("eth0", 65536, 1, 0)

count = 1
while count:
	(header, payload) = cap.next()
	print count
	count = count + 1