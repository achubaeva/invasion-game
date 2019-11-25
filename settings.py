
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
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3