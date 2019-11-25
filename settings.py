
import pygame

class Settings():
    '''A Class to store all settings for Alien Invasion Game'''
    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255,255,255)
        # Snail settings
        self.snail_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Mushroom settings
        self.mushroom_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 is right, -1 is left
        self.fleet_direction = 1