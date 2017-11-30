########################################################################
####					Class:Settings of Game						####
########################################################################
class Settings():
	#~ save all settings game need
	
	def __init__(self):
		#~ set screen
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (255,165,0)
		#~ self.bg_red=(255,0,0)
		#~ self.bg_green=(0,255,0)
		
		#~ set bullet
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 8

		#~ set level up scale
		self.speedup_scale = 1.5
		self.scoreup_scale = 2
		#~ set ship lifes
		self.ship_limit = 3
		
		self.game_active = False
		
		self.initialize_settings()
		self.restart_settings()
		
	def initialize_settings(self):
		#~ set sprite speed
		self.bullet_speed_factor = 1
		self.ship_speed_factor = 1.5
		self.alien_speed_factor = 0.5
		#~ set fleet speed
		self.fleet_drop_speed = 10
		self.fleet_speed_direction = 1
		#~ set score of aliens
		self.score_alien = 50
		
	def restart_settings(self):
		#~ reset ship lifes
		self.ship_left = self.ship_limit
		
		self.score = 0
		self.level = 1
		
	def increase_speed(self):
		self.bullet_speed_factor *= self.speedup_scale
		self.ship_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
	def increase_score(self):
		self.score_alien = int(self.score_alien * self.scoreup_scale)
