import pygame
from pygame.sprite import Sprite

class Mushroom(Sprite):
    '''A class to represent a single mushroom in the pack.'''

    def __init__(self, settings, screen):
        '''Initialize the mushroom and set its starting position.'''
        super(Mushroom, self).__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the mushroom image and set its rect attribute.
        self.image = pygame.image.load('Images/mushroom.png')
        self.rect = self.image.get_rect()

        # Start a new mushroom near the top of the left screen.
        self.rect.x = .5*self.rect.width
        self.rect.y = 10*self.rect.height

        # Store the mushroom's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        '''Draw the mushroom at its current location.'''
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        '''Move mushroom to the right or left'''
        self.x += (self.settings.mushroom_speed_factor*self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''Return True if mushroom at edge of screen.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True