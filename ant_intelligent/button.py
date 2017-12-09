########################################################################
####						Class:Button							####
########################################################################
import pygame

class StartButton():
	def __init__(self, game_settings, screen):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = game_settings
		self.font = pygame.font.SysFont(None, 48)
		self.txt = 'START'
		self.txt_color = (255, 255, 0)
		
		self.prep_startbutton()
	
	def prep_startbutton(self):
		self.image = self.font.render(self.txt, True,
							self.txt_color, self.game_settings.bg_color)
		self.image_rect = self.image.get_rect()
		self.image_rect.center = self.screen_rect.center
		
	def draw_startbutton(self):
		self.screen.blit(self.image,self.image_rect)
