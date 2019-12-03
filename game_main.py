import sys
import pygame
import game_functions as gf
from snail import Snail
from settings import Settings
from pygame.sprite import Group
from mushroom import Mushroom
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Garden Game")
    # Make a snail.
    snail = Snail(settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    # Make a mushroom group.
    mushrooms = Group()
    # Create instance to store game statistics and create a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Make the Play button
    play_button = Button(settings, screen, "Play")

    # Create grouping of mushrooms.
    gf.create_fleet(settings, screen, snail, mushrooms)

    # Start the main loop for the game.
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, snail, mushrooms, bullets)
        
        gf.update_screen(settings, screen, stats, sb, snail, mushrooms, bullets, play_button)

        if stats.game_active:
            snail.update()
            gf.update_bullets(settings, screen, stats, sb, snail, mushrooms, bullets)
            gf.update_mushrooms(settings, stats, screen, sb, snail, mushrooms, bullets)

run_game()
