import pygame

from pygame.sprite import Sprite

class Food(Sprite):

	def __init__(self,game_settings,screen):

		super(Food,self).__init__()
		self.game_settings = game_settings
		self.screen = screen
