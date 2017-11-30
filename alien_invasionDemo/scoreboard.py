########################################################################
####						Class:ScoreBoard						####
########################################################################
import pygame

class ScoreBoard():
	def __init__(self,game_settings,screen):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = game_settings
		
		self.scores_color = (155,155,155)
		self.font = pygame.font.SysFont(None,48)
		
		self.prep_score_level()
		
	def prep_score_level(self):
		rounded_score = int(round(self.game_settings.score,-1))
		score_str = "{:,}".format(rounded_score)
		level_str = str(self.game_settings.level)
		
		self.score_image = self.font.render(score_str,True,
						self.scores_color,self.game_settings.bg_color)
		self.level_image = self.font.render(level_str,True,
						self.scores_color,self.game_settings.bg_color)
							
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 10
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom 
		
	def show_score_level(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.level_image,self.level_rect)

class HighScore():
	def __init__(self,game_settings,screen):
		self.game_settings = game_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.score_color = (255,255,0)
		self.font = pygame.font.SysFont(None,48)
		self.high_score = 0
		
		self.prep_highscore()
	
	def prep_highscore(self):
		if self.game_settings.score > self.high_score:
			self.high_score = self.game_settings.score
		rounded_score = int(round(self.high_score,-1))
		highscore_str = "{:,}".format(rounded_score)
		self.highscore_image = self.font.render(highscore_str,True,
						self.score_color,self.game_settings.bg_color)
		self.rect = self.highscore_image.get_rect()
		self.rect.top = 10
		self.rect.centerx = self.screen_rect.centerx
		
	def show_highscore(self):
		self.screen.blit(self.highscore_image,self.rect)
