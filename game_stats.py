class GameStats():
    '''Track statistics for the game.'''

    def __init__(self, settings):
        '''Initialize stats.'''
        self.settings = settings
        self.reset_stats()
        # Start game in inactive state
        self.game_active = False
        self.high_score = 0
    
    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.snails_left = self.settings.snail_limit
        self.score = 0
        self.level = 1

    
