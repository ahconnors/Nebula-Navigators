import pygame
import sys
from pygame.locals import *
import math

# Add the missing import statement for screen_width and screen_height
# Initialize screen_width and screen_height with appropriate values
screen_width = 1500
screen_height = 850

import pygame
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()
        self.original_image = pygame.image.load('Player.webp').convert_alpha()  # Load player image
        self.image = pygame.transform.scale(self.original_image, (75, 75))
        self.cleanImage=self.image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Start position
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.angle= (math.pi)/2
        
    def accelerate(self, rot, acceleration):
        self.angle += rot 
        self.image = rot_center(self.cleanImage, (self.angle*180/math.pi)-90)
        self.acceleration_x = -acceleration*math.cos(self.angle)
        self.acceleration_y = acceleration*math.sin(self.angle)

    def update(self):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        


        # Update position based on velocity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Keep the player on the screen
        self.rect.x = max(0, min(self.rect.x, 1500 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 850 - self.rect.height))
        self.check_border_collision()
    
    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def check_border_collision(self):
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.velocity_x = 0
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.velocity_y = 0
