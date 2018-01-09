import sys

import pygame

background_image_filename = 'background.jpg'
mouse_image_filename = 'mouse.png'

pygame.init()

screen=pygame.display.set_mode((1366,768))
pygame.display.set_caption("hello world")

background=pygame.image.load(background_image_filename)
mouse_cursor=pygame.image.load(mouse_image_filename)

while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	screen.blit(background,(0,0))
	x, y = pygame.mouse.get_pos()
	
	x -= mouse_cursor.get_width()/2
	y -= mouse_cursor.get_height()/2
	screen.blit(mouse_cursor,(x,y))
	
	pygame.display.update()

