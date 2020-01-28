import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, ship, screen, bullets):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            #spaceship moving
            check_keypress_events(event, ship, screen, bullets, ai_settings)

def check_keypress_events(event, ship, screen, bullets, ai_settings):
    '''respond to all keypresses'''
    #keypress
    if event.type == pygame.KEYDOWN:
        #quit
        if event.key == pygame.K_q:
            sys.exit()
        
        #ship keypress
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        
        #bullet keypress
        if event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            if len(bullets) < ai_settings.bullets_allowed:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)


    #ship key releases
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def create_fleet(ai_settings, screen, aliens, ship):
    '''Create a full fleet of aliens'''
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_wigth - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    number_rows = get_number_rows(ai_settings, ship.ship_rect.height, alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    
def get_number_rows(ai_settings, ship_height, alien_height):
    '''determine the number of rows of aliens that fit on the screen'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''create a single alien'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_bullets(bullets):
    #calls bullet.update() for each bullet we place in the group bullets
        bullets.update()

        #get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.bul_rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

def update_aliens(ai_settings, aliens):
    '''update the positions of all aliens in the fleet'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    '''respond appropriately if anu aliens have reached and edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''drop the entire fleet and change the fleet's direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

    
def update_screen(ai_settings, screen, ship, bullets, aliens):
    '''Draw screen and elements'''
    screen.fill(ai_settings.bg_color)

    ship.draw_ship()
    #alien.draw_alien()
    aliens.draw(screen)

    update_bullets(bullets)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()
    #clock.tick(30)