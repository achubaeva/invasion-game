
import pygame

class Snail():

    def __init__(self, settings, screen):
        '''Initialize the snail and setits starting position.'''
        self.screen = screen
        self.settings = settings
        # Load the snail image and get its rect.
        self.image = pygame.image.load('Images/snail.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new snail at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on the movement flags'''
        # Update the ship's center value, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.snail_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.snail_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        '''Draw the snail at its current location.'''
        self.screen.blit(self.image, self.rect)

    def center_snail(self):
        '''Center the snail on the screen'''
        self.center = self.screen_rect.centerx 