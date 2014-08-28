import thread
import time 
import pygame
from pygame.locals import *
from sys import exit
from pygame.color import THECOLORS
from Client import Client

background_image = 'image/background.png'

def draw_go(c1):
	if c1.update_flag == True:
		c1.update_flag = False

		screen.blit(background, (0,0))
		board = c1.get_board() 


		p = 32.4

		i = 1
		while i<=19:
			j = 1
			while j<=19:
				id =  board[i*21 + j]

				if id=="1":
					pygame.draw.circle(screen,THECOLORS["black"],[int(p*j),int(p*(20-i))],15,0)
					pygame.draw.circle(screen,THECOLORS["gray"],[int(p*j),int(p*(20-i))],15,1)
				elif id=="3":
					pygame.draw.circle(screen,THECOLORS["white"],[int(p*j),int(p*(20-i))],15,0)
					pygame.draw.circle(screen,THECOLORS["gray"],[int(p*j),int(p*(20-i))],15,1)
				j+=1
			i+=1
					
		pygame.display.update()

c1 = Client()


pygame.init()

screen = pygame.display.set_mode((645, 645), 0, 32)
pygame.display.set_caption(c1.state.Name)

background = pygame.image.load(background_image).convert()

screen.blit(background, (0,0))
pygame.display.update()




while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type == MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()

			print "[56] Mouse click"
			print pos
			print 20 - int(pos[1]/33.95+1), int(pos[0]/33.95+1)
			
			print c1.update_flag
			if c1.update_flag == False:
				c1.update_flag = True
				c1.send_station(20 - int(pos[1]/33.95+1), int(pos[0]/33.95+1))
			print "[58] Client send"

	draw_go(c1)
			
	time.sleep(0.1)

