import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port=3101
s.connect(("localhost",port))
for i in xrange(5):
  
  inp=raw_input("Enter message")
  print 'send server:'
  s.send(inp)
  #s.close()