import pygame
import sys
from pygame.locals import *

# Add the missing import statement for screen_width and screen_height
# Initialize screen_width and screen_height with appropriate values
screen_width = 800
screen_height = 600

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('Player.webp').convert_alpha()  # Load player image
        self.image = pygame.transform.scale(self.original_image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Start position
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        
    def accelerate(self, acceleration_x, acceleration_y):
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y

    def update(self):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y


        # Update position based on velocity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Keep the player on the screen
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))
    
    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y
