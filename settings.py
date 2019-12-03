
import pygame

class Settings():
    '''A Class to store all settings for Alien Invasion Game'''
    def __init__(self):
        '''Initialize the game's static settings.'''
        
        # Screen settingss
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (226, 254, 226)
        
       
        
        # Bullet settings
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Mushroom settings
        self.fleet_drop_speed = 10

        self.snail_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the point value increases
        self.score_scale = 1.5

        

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game.'''
         # Snail settings
        self.snail_speed_factor = 2
        self.bullet_speed_factor = 3
        self.mushroom_speed_factor = 2
        # 1 is right, -1 is left
        self.fleet_direction = 1

        # Scoring
        self.mushroom_points = 50

    def increase_speed(self):
        '''Increase speed settings and point values.'''
        self.snail_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.mushroom_speed_factor *= self.speedup_scale

        self.mushroom_points = int(self.mushroom_points*self.score_scale)

