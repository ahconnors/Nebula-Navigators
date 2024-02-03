import pygame
import sys
from pygame.locals import *

# Add the missing import statement for screen_width and screen_height
# Initialize screen_width and screen_height with appropriate values
screen_width = 800
screen_height = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('rocket.svg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.velocity = pygame.Vector2(0, 0)

    def accelerate(self, acceleration_x, acceleration_y):
        self.velocity.x += acceleration_x
        self.velocity.y += acceleration_y

    def update(self):
        self.rect.move_ip(self.velocity)
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))