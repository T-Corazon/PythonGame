########################################################################
####						Class:Ship								####
########################################################################
import pygame

class Ship():
	
	def __init__(self,game_settings,screen):
		#~ define ship & position of ship
		self.screen = screen
		
		#~ load image & obtain rect
		self.image = pygame.image.load('image/boy.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.game_settings = game_settings
		
		self.width = self.image.get_width()
		self.shipleft_rect = self.image.get_rect()
		
		#~ put ship at the bottom,center
		# center,centerx,centery
		self.rect.centerx = self.screen_rect.centerx
		# top,bottom,left,right
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
		
		#~ moving flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def update(self):
		
		if self.moving_right:
			if self.rect.right <= self.screen_rect.right:
				self.center += self.game_settings.ship_speed_factor
			else:
				self.center -= self.game_settings.ship_speed_factor
		if self.moving_left:
			if self.rect.left >= self.screen_rect.left:
				self.center -= self.game_settings.ship_speed_factor
			else:
				self.center += self.game_settings.ship_speed_factor
		if self.moving_up:
			if self.rect.top >= self.screen_rect.top:
				self.bottom -= self.game_settings.ship_speed_factor
			else:
				self.bottom += self.game_settings.ship_speed_factor
		if self.moving_down:
			if self.rect. bottom <= self.screen_rect.bottom:
				self.bottom += self.game_settings.ship_speed_factor
			else:
				self.bottom -= self.game_settings.ship_speed_factor
		
		self.rect.centerx = self.center
		self.rect.bottom = self.bottom
		
	def center_ship(self):
		self.center = self.screen_rect.centerx
		self.bottom = self.screen_rect.bottom
	
	def blitme(self):
		#~ print ship at right place
		self.screen.blit(self.image,self.rect)
	
	def blit_ship_left(self):
		if self.game_settings.ship_left > 0:
			for ship_left in range(self.game_settings.ship_left):
				self.shipleft_rect.top = 0
				self.shipleft_rect.left = self.width * ship_left
				self.screen.blit(self.image,self.shipleft_rect)
