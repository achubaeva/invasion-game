import pygame.font
from pygame.sprite import Group
from snail import Snail
import settings as Settings

class Scoreboard():
    '''A class to report scoring information.'''

    def __init__(self, settings, screen, stats):
        '''Initialize scorekeeping attributes.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring info.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)

        # Prepare initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_snails()

    def prep_score(self):
        '''Turn the score into rendered image.'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score: "+score_str, True, self.text_color, self.settings.bg_color)

        # Display score at top right of screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''Turn the high score into a rendered image.'''
        rounded_high_score = int(round(self.stats.score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render("High Score: "+high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = 20+ (self.settings.screen_width/2)
        self.high_score_rect.top = 20

    def prep_level(self):
        '''Turn the level into a rendered image.'''
        self.level_image = self.font.render("Level: "+str(self.stats.level), True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        '''Draw scores to screen.'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw snails
        self.snails.draw(self.screen)

    def prep_snails(self):
        '''Show how many snails are left.'''
        self.snails = Group()
        for snail_number in range(self.stats.snails_left):
            snail = Snail(self.settings, self.screen)
            snail.rect.x = 10 + snail_number * snail.rect.width
            snail.rect.y = 10
            self.snails.add(snail)

    