import pygame
import sys
from rocket import Player

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define acceleration constants
ACCELERATION_X = 0.01
ACCELERATION_Y = 0.01

def Main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Nebula Navigators')
    pygame_icon = pygame.image.load('rocket.svg')
    pygame.display.set_icon(pygame_icon)

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

        # Apply acceleration
        acceleration_x = dx * ACCELERATION_X
        acceleration_y = dy * ACCELERATION_Y

        # Update player velocity based on acceleration
        player.accelerate(acceleration_x, acceleration_y)

        # Update player position
        player.update()

        # Clear the screen
        screen.fill(BLACK)

        # Draw player
        screen.blit(player.image, player.rect)

        # Refresh display
        pygame.display.flip()

if __name__ == '__main__':
    Main()
