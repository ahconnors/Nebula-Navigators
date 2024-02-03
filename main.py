import pygame
import sys

def Main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Nebula Navigators')
    pygame_icon = pygame.image.load('rocket.svg')
    pygame.display.set_icon(pygame_icon)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))
        pygame.display.flip()

if __name__ == '__main__':
    Main()