import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

########################################################################
####					Function:CreatBullets						####
########################################################################

def fire_bullet(game_settings,screen,ship,bullets):
	if len(bullets) < game_settings.bullets_allowed:
		new_bullet = Bullet(game_settings,screen,ship)
		bullets.add(new_bullet)

########################################################################
####					Function:CreatFleet							####
########################################################################

def get_number_alien_x(game_settings,alien_width):
	available_space_x = (game_settings.screen_width - 
							(2 * alien_width))
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(game_settings,alien_height,ship):
	available_space_y = (game_settings.screen_height - 
							(8 * alien_height) - ship.rect.height)
	number_rows = int(available_space_y / alien_height)
	return number_rows

def create_fleet(game_settings,screen,aliens,ship):
	alien = Alien(game_settings,screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	
	number_aliens_x = get_number_alien_x(game_settings,alien_width)
	number_rows = get_number_rows(game_settings,alien_height,ship)
	for alien_row in range(number_rows):
		for alien_number in range(number_aliens_x):
			alien = Alien(game_settings,screen)
			alien.x += 2 * alien_width * alien_number
			alien.rect.x = alien.x
			alien.rect.y += alien_height * alien_row
			aliens.add(alien)

########################################################################
####					Function:FleetActions						####
########################################################################

def check_fleet_edges(game_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(game_settings,aliens)
			break
			
def change_fleet_direction(game_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += game_settings.fleet_drop_speed
	game_settings.fleet_speed_direction *= -1

########################################################################
####					Function:SpyKeyboard						####
########################################################################

def check_keydown_events(event,game_settings,screen,ship,bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			ship.moving_left = True
		elif event.key == pygame.K_UP:
			ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			ship.moving_down = True

		elif event.key == pygame.K_SPACE:
			fire_bullet(game_settings,screen,ship,bullets)
	
def check_keyup_events(event,ship):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			ship.moving_left = False
		elif event.key == pygame.K_UP:
			ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			ship.moving_down = False
def check_pause_event(event,game_settings):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_p:
			game_settings.game_active = not game_settings.game_active

########################################################################
####					Function:SpyAllEvents						####
########################################################################

def check_events(game_settings,play_button,
					screen,ship,bullets,aliens,score):
	#~ get event from keyboard and mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		check_pause_event(event,game_settings)
		check_keydown_events(event,game_settings,screen,ship,bullets)
		check_keyup_events(event,ship)
		#~ check mousebuttondown
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(game_settings,screen,aliens,bullets,ship,
									score,play_button,mouse_x, mouse_y)

def check_play_button(game_settings,screen,aliens,bullets,ship,score,
									play_button,mouse_x, mouse_y):
							
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not game_settings.game_active:
		reset_settings(game_settings,aliens,bullets,screen,ship,score)

def reset_settings(game_settings,aliens,bullets,screen,ship,score):
	pygame.mouse.set_visible(False)
	
	game_settings.restart_settings()
	score.prep_score_level()
	
	game_settings.initialize_settings()
	game_settings.game_active = True
		
	aliens.empty()
	bullets.empty()
		
	create_fleet(game_settings,screen,aliens,ship)
	ship.center_ship()

#~ if game_settings.ship_left == 0:
########################################################################
####					Function:ShipDownSituation					####
########################################################################
def ship_hited(game_settings,ship):
	game_settings.ship_left -= 1
	ship.center_ship()
	
	sleep(0.2)

def alien_down(game_settings,screen,ship,aliens):
	game_settings.ship_left -= 1
	aliens.empty()
	create_fleet(game_settings,screen,aliens,ship)
	ship.center_ship()
	
	sleep(0.2)
	
########################################################################
####					Function:SpritesCollosions					####
####	Action:Spy collisions of sprites,Scoring,Set level of game	####
########################################################################

def sprites_collisions(game_settings,screen,ship,
									bullets,aliens,score,highscore):
	check_alien_bullet_collision(game_settings,screen,ship,aliens,
											bullets,score,highscore)
	#~ ship alien collide
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hited(game_settings,ship)
		
	check_fleet_get_bottom(game_settings,screen,ship,aliens)
	
	if game_settings.ship_left == 0:
		game_settings.game_active = False
		pygame.mouse.set_visible(True)

def check_alien_bullet_collision(game_settings,screen,ship,aliens,
											bullets,score,highscore):
	collisions = pygame.sprite.groupcollide(aliens,bullets,True,True)
	if collisions:
		for aliens in collisions.values():
			game_settings.score += (game_settings.score_alien * 
														len(aliens))
			score.prep_score_level()
			highscore.prep_highscore()
	if len(aliens) == 0:
		game_settings.increase_speed()
		game_settings.increase_score()
		create_fleet(game_settings,screen,aliens,ship)
		
		game_settings.level += 1
		
def check_fleet_get_bottom(game_settings,screen,ship,aliens):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			alien_down(game_settings,screen,ship,aliens)
			break

########################################################################
####					Function:UpdateSprites						####
########################################################################

def update_aliens(game_settings,screen,aliens,ship):
	check_fleet_edges(game_settings,aliens)
	aliens.update(game_settings)
	
def update_bullets(bullets):
	bullets.update()
	#~ delete bullets out of screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

########################################################################
####				Function:UpdateScreenOrResetGame				####
########################################################################

def update_screen(game_settings,screen,ship,aliens,bullets,
									play_button,score,highscore):
	#~ set background color
	screen.fill(game_settings.bg_color)
	
	score.show_score_level()
	highscore.show_highscore()
	# draw bullets
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	ship.blit_ship_left()
	aliens.draw(screen)
	
	if not game_settings.game_active:
		play_button.draw_button()
	#~ refresh screen
	pygame.display.flip()
