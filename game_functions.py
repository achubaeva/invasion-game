import sys
import pygame
from bullet import Bullet
from mushroom import Mushroom

def check_keydown_events(event, settings, screen, snail, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the snail to the right.
        snail.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the snail to the left.
        snail.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, snail, bullets)
    elif event.key == pygame.K_q:
            pygame. quit()
            sys.exit

def fire_bullet(settings, screen, snail, bullets):
    '''Fire a bullet if limit not reached yet.'''
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, screen, snail)
            bullets.add(new_bullet)

def check_keyup_events(event, snail):
    if event.key == pygame.K_RIGHT:
        snail.moving_right = False
    elif event.key == pygame.K_LEFT:
        snail.moving_left = False

def check_events(settings, screen, snail, bullets):
    '''Respond to keypresses and mouse events.'''
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, snail, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, snail)
        

def update_screen(settings, screen, snail, mushrooms, bullets):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    
    # Redraw all bullets behind snail and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    snail.blitme()
    mushrooms.draw(screen)
    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    '''Update the position of bullets and get rid of old bullets.'''
    # update bullet positions.
    # Get rid of bullets that have dissappeared.
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def create_fleet(settings, screen, mushrooms):
    '''Create fleet of mushrooms.'''
    # Create a mushroom and find the number of mushrooms in a row.
    # Spacing between each mushroom is equal to 1/2 mushroom width.
    mushroom = Mushroom(settings, screen)
    mushroom_width = mushroom.rect.width
    available_space_x = settings.screen_width - 2 * (.5*mushroom_width)
    number_mushrooms_x = int(available_space_x / (2*mushroom_width))

    # Create the first row of mushrooms.
    for mushroom_number in range(number_mushrooms_x):
        # Create a mushroom and place it in the row
        mushroom = Mushroom(settings, screen)
        mushroom.x = mushroom_width + 2 * mushroom_width * mushroom_number
        mushroom.rect.x = mushroom.x
        mushrooms.add(mushroom)