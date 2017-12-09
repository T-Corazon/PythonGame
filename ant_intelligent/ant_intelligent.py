import pygame

from game_functions import *
import game_functions as gf
from pygame.sprite import Group

from game_settings import GameSettings
from button import StartButton

########################################################################
####					Function:Main Program						####
########################################################################

def run_program():
	
	pygame.init()
	game_settings = GameSettings()
	
	screen = pygame.display.set_mode(
			(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Ant Intelligent")
	
	start_button = StartButton(game_settings, screen)
	
	ants = Group()
	foods = Group()
	
########################################################################
####					Function:Main Loop							####
########################################################################
	while True:
		gf.check_all_event(game_settings, start_button)
		
		if game_settings.game_active:
			pass
		
		gf.screen_update(game_settings,screen,start_button)
		
########################################################################
####					Action:Run Program							####
########################################################################
run_program()
