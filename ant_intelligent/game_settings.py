########################################################################
####						Class:GameSettings						####
########################################################################
class GameSettings():
	def __init__(self):
		self.screen_width,self.screen_height = (640,480)
		self.bg_color = (0,0,0)
		
		self.game_active = False
		
		self.ant_limit = 5
		self.food_limit = 3
		self.food_size_limit = 40
		
		self.initilize_settings()
	
	def initilize_settings(self):
		None
