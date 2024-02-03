import pygame
import sys
from planet import Planet

class Planet:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        pass

    def check_collision(self, player):
        distance = ((self.x - player.rect.x) ** 2 + (self.y - player.rect.y) ** 2) ** 0.5
        return distance < self.radius + player.rect.width / 2

    def handle_collision(self, player):
        player.rect.x = 400
        player.rect.y = 300
        player.velocity_x = 0
        player.velocity_y = 0
        player.acceleration_x = 0
        player.acceleration_y = 0
        player.lives -= 1
        if player.lives == 0:
            return GameState.GAME_OVER
        return GameState.PLAYING