class GameStats():
    """The role of the class is to manage the game stats"""
    
    def __init__(self, ai_settings):
	    #data init
	    self.ai_settings = ai_settings
	    self.reset_stats()
	    self.game_active = False
	    self.high_score = 0
	    
    def reset_stats(self):
	    #stats init
	    self.ships_left = self.ai_settings.ship_limit
	    self.score = 0
	    self.level = 1
   
   
