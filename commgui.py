import pygame
from time import *
import thread
from socket import *
from textbox import TextBox 
from pygame import gfxdraw

IP="127.0.0.1"
PORT=5005
size=1024
white=(255,255,255)
black=(0,0,0)	
blue=(135,206,250)
datas = []
def server():
	while True:
		s=socket(AF_INET,SOCK_STREAM)
		s.bind((IP,PORT))
		s.listen(1)
		conn,addr=s.accept()

		while True:
			data=conn.recv(size)
			if not data:
				break
			#print strftime("|%d.%m.%y|%H:%M:%S|:", localtime()), data
			datas.append(strftime("|%H:%M:%S|: ", localtime())+ data)

			conn.send(data)
		conn.close()
		
def client():
	while True:
		#message=raw_input(": ")
		s=socket(AF_INET,SOCK_STREAM)
		s.connect((IP,PORT))
		s.send(message)
		datas.append(message)
		data=s.recv(size)
		s.close()



	
IP="127.0.0.1"
PORT1=5005
PORT2=5005
size=40

try:
	thread.start_new_thread(server,())
	#thread.start_new_thread(client,())
except:
	print "error"

res=[840,640]
pygame.init()
window=pygame.display.set_mode(res)
clock=pygame.time.Clock()




def draw():
	window.fill(white)
	for i in range(len(datas)):
		Font=pygame.font.SysFont("arial",24)
		text = Font.render(str(datas[i]),True,black)
		if datas[i][0]=='|':
			pygame.gfxdraw.filled_ellipse(window,25,40*(i-len(datas)+12)+10,20*len(datas[i]),35,blue)
			#pygame.gfxdraw.aaellipse(window,-30,40*(i-len(datas)+12)-15,20*len(datas[i]),55,black)
			window.blit(text,(25,(i-len(datas)+12)*40))	
		else:
			pygame.gfxdraw.filled_ellipse(window,450,40*(i-len(datas)+12)+10,20*len(datas[i]),35,blue)
			#pygame.draw.ellipse(window,blue,pygame.Rect(390,40*(i-len(datas)+12)-15,20*len(datas[i]),55),0)
			#pygame.gfxdraw.ellipse(window,black,pygame.Rect(390,40*(i-len(datas)+12)-15,20*len(datas[i]),55),2)
			window.blit(text,(450,(i-len(datas)+12)*40))	
			
def send(idn,text):
	#message=raw_input(": ")
	message=str(text)
	s=socket(AF_INET,SOCK_STREAM)
	s.connect((IP,PORT))
	s.send(message)
	datas.append(message)
	data=s.recv(size)
	s.close()
	

timerbox=TextBox((0,590,840,40),command=send,clear_on_enter=True,inactive_on_enter=False)

end=False
while not end:
	for z in pygame.event.get():
		if z.type==pygame.QUIT:
			end=True
		timerbox.get_event(z)

	draw()
	timerbox.update()
	timerbox.draw(window)
	clock.tick(20)
	pygame.display.flip()

