########################################################################
####					Function:All Functions						####
########################################################################
import sys
import pygame

from ant import Ant
from food import Food

########################################################################
####					Function:Spy All Events						####
########################################################################

def check_all_event(game_settings,start_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		check_start_button(game_settings,event,start_button)
		check_pause_event(game_settings,event,start_button)

def check_pause_event(game_settings,event,start_button):
	if game_settings.game_active:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				pygame.mouse.set_visible(True)
				game_settings.game_active = False
	else:
		if event.type == pygame.KEYDOWN:
			game_settings.game_active = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			button_clicked = (start_button.
							image_rect.collidepoint(mouse_x, mouse_y))
			if button_clicked:
				game_settings.game_active = True
			
def check_start_button(game_settings,event,start_button):
	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_x,mouse_y = pygame.mouse.get_pos()
		button_clicked = (start_button.
							image_rect.collidepoint(mouse_x, mouse_y))
		if button_clicked and not game_settings.game_active:
			restart_game(game_settings)
			
def restart_game(game_settings):
	pygame.mouse.set_visible(False)
	
	game_settings.initilize_settings()
	game_settings.game_active = True


########################################################################
####					Function:Spy All Events						####
########################################################################
def screen_update(game_settings,screen,start_button):
	screen.fill(game_settings.bg_color)
	
	update_start_button(game_settings,start_button)
		
	pygame.display.flip()
	
def update_start_button(game_settings,start_button):
	if not game_settings.game_active:
		start_button.prep_startbutton()
		start_button.draw_startbutton()
		
########################################################################
####				Function:Creat Ants and Foods
					####
########################################################################

def create_ants(game_settings,screen,ants):
	ants_num = game_settings.ant_limit
	for ant_num in range(ants_num):
		new_ant = Ant(game_settings,screen)
		ants.add(new_ant)

def create_foods(game_settings,screen,foods):
	foods_num = game_settings.food_limit
	for food_num in range(foods_num):
		new_food = Food(game_settings,screen)
		Food.add(new_food)
