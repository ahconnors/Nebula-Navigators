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
<<<<<<< Updated upstream
        self.image = pygame.transform.scale(self.original_image, (75, 75))
        self.cleanImage=self.image
        self.rect = self.image.get_rect()
        self.rect.center = (800, 600)  # Start position
=======
        self.lit_image = pygame.image.load('litRocket.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (75, 75))
        self.lit_image = pygame.transform.scale(self.lit_image, (75, 75))
        self.image = self.original_image
        self.cleanImage=self.original_image
        self.rect = self.original_image.get_rect()
        self.rect.center = (400, 300)  # Start position
>>>>>>> Stashed changes
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.angle= (math.pi)/2
        self.posx=0
        self.posy=0 
        
    def accelerate(self, rot, acceleration):
        self.angle += rot 
<<<<<<< Updated upstream
        self.image = rot_center(self.cleanImage, (self.angle*180/math.pi)-90)
        self.acceleration_x = -acceleration*math.cos(self.angle)
        self.acceleration_y = acceleration*math.sin(self.angle)
=======
        self.image = rot_center(self.cleanImage, (self.angle * 180 / math.pi) - 90)
        self.acceleration_x = -acceleration * math.cos(self.angle)
        self.acceleration_y = acceleration * math.sin(self.angle)

        # Check if either acceleration_x or acceleration_y is positive

        # Scale the image to keep it consistent with the size of the original image
        self.image = pygame.transform.scale(self.image, (75, 75))
>>>>>>> Stashed changes

    def update(self):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        


        # Update position based on velocity
        self.posx += self.velocity_x
        self.posy += self.velocity_y

        # Keep the player on the screen
        self.check_border_collision()
    
    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def check_border_collision(self):
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.velocity_x = 0
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.velocity_y = 0
