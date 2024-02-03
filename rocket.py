import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('rocket.svg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Start position
        self.speed = 5

    def update(self, dx, dy):
        # Update position based on input
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Keep the player on the screen
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))