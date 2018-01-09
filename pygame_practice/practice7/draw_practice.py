import sys

import pygame
from random import randint
from math import pi

pygame.init()
screensize=(1200,600)

screen=pygame.display.set_mode(screensize,0,32)
pygame.display.set_caption("Draw Practice")
points=[]



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			points.append((x,y))
			
			#~ draw a rect
			color_random = (randint(0,255),randint(0,255),randint(0,255))
			pos_first = (randint(0,399),randint(0,299))
			pos_last = (randint(0,399-pos_first[0]),randint(0,299-pos_first[1]))
			pygame.draw.rect(screen,color_random,(pos_first,pos_last))
			pygame.draw.rect(screen,color_random,[50,50,50,50])
			#~ draw a ellipse
			color_random = (randint(0,255),randint(0,255),randint(0,255))
			pos_first = (randint(400,799),randint(0,299))
			pos_last = (randint(0,799-pos_first[0]),randint(0,299-pos_first[1]))
			pygame.draw.ellipse(screen,color_random,(pos_first,pos_last))
			#~ draw a polygon
			#~ if len(points) > 2:
				#~ color_random = (randint(0,255),randint(0,255),randint(0,255))
				#~ pygame.draw.polygon(screen,color_random,points)
			#~ draw a circle
			color_random = (randint(0,255),randint(0,255),randint(0,255))
			pos_circle = (randint(800,1199),randint(0,299))
			radius=randint(1,10)
			pygame.draw.circle(screen,color_random,pos_circle,radius)
			#~ draw a arc
			try:
				color_random = (randint(0,255),randint(0,255),randint(0,255))
				pos_first = (randint(0,399),randint(300,599))
				pos_last = (randint(0,399-pos_first[0]),randint(0,599-pos_first[1]))
				pygame.draw.arc(screen,color_random,(pos_first,pos_last),0,pi/2)
			except ValueError:
				pass
			else:
				pass
			#~ draw a line
			color_random = (randint(0,255),randint(0,255),randint(0,255))
			pos_first = (randint(400,799),randint(300,599))
			pos_last = (randint(400,799),randint(300,599))
			pygame.draw.line(screen,color_random,pos_first,pos_last,1)
			#~ draw lines
			if len(points) > 2:
				color_random = (randint(0,255),randint(0,255),randint(0,255))
				pygame.draw.lines(screen,color_random,False,points,6)

	pygame.display.flip()
