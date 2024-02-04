import pygame
import sys
from pygame.locals import *
import math



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
    #def flame(self):
      #  self.cleanImage=self.lit_image
   # def unflame(self):
        #self.cleanImage=self.original_image
    def __init__(self,resX,resY):
        super().__init__()
        self.original_image = pygame.image.load('Player.webp').convert_alpha()  # Load player image
        #self.lit_image = pygame.image.load('Player.webp').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (75, 75))
        #self.lit_image = pygame.transform.scale(self.lit_image, (25, 75))
        self.image = self.original_image
        self.cleanImage=self.original_image
        self.rect = self.original_image.get_rect()
        self.rect.center = (resX/2, resY/2)  # Start position
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.posx= 0
        self.posy= 0
        self.angle= (math.pi)/2
        self.posx=0
        self.posy=0
        
        self.landed = False
        self.gettingFuel = False
        self.gettingOxygen = False
        self.gettingWater = False
        self.gettingSteel = False
    

    def accelerate(self, rot, acceleration):
        self.angle += rot 
        self.image = rot_center(self.cleanImage, (self.angle * 180 / math.pi) - 90)
        self.acceleration_x = -acceleration * math.cos(self.angle)
        self.acceleration_y = acceleration * math.sin(self.angle)

        # Check if either acceleration_x or acceleration_y is positive

        # Scale the image to keep it consistent with the size of the original image

    def update(self):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        
        #if(self.acceleration_x == 0 and self.acceleration_y == 0):
            #self.unflame()

        # Update position based on velocity
        self.posx += self.velocity_x
        self.posy += self.velocity_y

        # Check validity of position
        #self.posx = max()

    
    def setPos(self, x, y):
        self.posx = x
        self.posy = y
