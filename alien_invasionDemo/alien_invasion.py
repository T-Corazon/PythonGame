########################################################################
####					Programe:Aline Invasion						####
########################################################################
import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import ScoreBoard,HighScore
import game_functions as gf
from time import sleep

########################################################################
####					Function:MainPrograme						####
########################################################################

def run_game():
	
	#~ open and define screen
	pygame.init()
	game_settings = Settings()
	
	screen = pygame.display.set_mode(
		(game_settings.screen_width,game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#~ creat a ship
	ship = Ship(game_settings,screen)
	#~ creat bullets & aliens
	bullets = Group()
	aliens = Group()
	
	play_button = Button(game_settings,screen,"PLAY")
	score = ScoreBoard(game_settings,screen)
	highscore = HighScore(game_settings,screen)
	
	gf.create_fleet(game_settings,screen,aliens,ship)
	
	
	
########################################################################
####					Function:MainLoop							####
########################################################################

	while True:
		gf.check_events(game_settings,play_button,
							screen,ship,bullets,aliens,score)
		
		if game_settings.game_active:
			ship.update()
			gf.update_aliens(game_settings,screen,aliens,ship)
			gf.update_bullets(bullets)
			gf.sprites_collisions(game_settings,screen,
									ship,bullets,aliens,score,highscore)
									
		gf.update_screen(game_settings,screen,ship,aliens,
									bullets,play_button,score,highscore)
		
		
run_game()
