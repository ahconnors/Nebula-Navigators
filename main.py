import pygame
import sys

def Main:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('My Game')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        pygame.display.flip()