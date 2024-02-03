import pygame
import sys
from rocket import Player

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def Main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Nebula Navigators')
    pygame_icon = pygame.image.load('rocket.svg')
    pygame.display.set_icon(pygame_icon)
    background = pygame.image.load('Background.png')
    background = pygame.transform.scale(background, (800, 600))
    # Create player object
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get user input
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        # Clear the screen
        screen.fill(BLACK)

        # Update player position
        player.update(dx, dy)

        # Draw background
        screen.blit(background, (0,0))
        # Draw player
        screen.blit(player.image, player.rect)

        # Refresh display
        pygame.display.flip()

if __name__ == '__main__':
    Main()

