import thread
from socket import *
from time import *

IP="127.0.0.1"
PORT1=5005
PORT2=5005
size=1024

def server():

	while True:
		s=socket(AF_INET,SOCK_STREAM)
		s.bind((IP,PORT1))
		s.listen(1)
		conn,addr=s.accept()

		while True:
			data=conn.recv(size)
			if not data:
				break
			print strftime("|%d.%m.%y|%H:%M:%S|:", localtime()), data
			conn.send(data)
		conn.close()
		
def client():
	IP="127.0.0.1"
	PORT=5005
	size=1024

	while True:
		message=raw_input(": ")
		s=socket(AF_INET,SOCK_STREAM)
		s.connect((IP,PORT2))
		s.send(message)
		data=s.recv(size)
		s.close()
		
		
		
		
		
try:
	thread.start_new_thread(server,())
	thread.start_new_thread(client,())
except:
	print "error"
	
while True:
	pass