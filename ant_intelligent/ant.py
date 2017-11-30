########################################################################
####						Class:SpirteAnt							####
########################################################################
import pygame

from pygame.sprite import Sprite

class Ant(Sprite):
	
	def __init__(self,game_settings,screen):
		
		super(Ant,self).__init__()
			
			self.game_settings = game_settings
			self.screen = screen
			
			self.body_size = (1,1)
			self.color = (255,255,255)
			self.load_capability = 4
			
########################################################################
####					Function:Action Module						####
####	Action:Define searching,following and transporting			####
####			Use action_flag to make the decision for ants		####
########################################################################

	def get_action_flag(self):
		action_flag = 'S' or 'F' or 'T'
		return action_flag

	def ant_action_excute(self):
		#~ use a function to get action_flag
		action_flag = get_action_flag()
		if action_flag == 'S':
			search_mod()
		if action_flag == 'F':
			follow_mod()
		if action_flag == 'T':
			transport_mod()

	def search_mod(self):
		
		smell_normal_mod()

	def follow_mod(self):
		
		smell_none_mod()

	def transport_mod(self):
		
		smell_double_mod()

########################################################################
####					Function:Smell Module						####
####	Action:Define the smell of search,follow and transport.	####
########################################################################

def smell_none_mod(self):
	

def smell_normal_mod(self):
	

def smell_double_mod(self):
