import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"

port=3101

s.bind(('localhost',port))

s.listen(5)
print "socket listening"
c,addr=s.accept()
while 1:
	#print "listening for client"
	
	#print 'Got connection' , addr
	st = c.recv(1024);
	if st:
		#print "Message received"
		print st
	#c.close()	 
	#c.send('Mandir yahi banega')
	