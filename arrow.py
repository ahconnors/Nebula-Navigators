import pygame
import sys
from pygame.locals import *
import math


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
class Arrow(pygame.sprite.Sprite):
    def __init__(self,resX,resY):
        super().__init__()
        self.resX = resX
        self.resY = resY
        self.original_image = pygame.image.load('Arrow.png')  # Load player image
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))
        #self.image = self.original_image
        self.cleanImage=self.original_image
        self.rect=(resX+60,resY)
        self.angle= math.pi/2
    
    def point(self,angle):
        self.angle=angle
        self.rect=(self.resX/2-60*+math.cos(self.angle)-50,self.resY/2+math.sin(self.angle)*60-50)
        self.image = rot_center(self.cleanImage, -self.angle*180/math.pi+90)
    