import pygame
import sys
import math
class Planet:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_collision = 0
        self.y_collision = 0
        self.collisionRadius = 0
        self.centerx = 0
        self.centery = 0

    def draw(self, screen):
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        pass

    def check_collision(self, player):
        self.centerx = player.rect.x + player.rect.width / 2
        self.centery = player.rect.y + player.rect.height / 2
        distance = ((self.x - self.centerx) ** 2 + (self.y - self.centery) ** 2) ** 0.5
        self.collisionRadius = distance
        if(distance < (self.radius + player.rect.width / 2)):
            self.x_collision = self.centerx - self.x
            self.y_collision= -(self.centery - self.y)
            print(self.x_collision, self.y_collision)
        return distance < self.radius + player.rect.width / 2

    def handle_collision(self, player):
        collisionAngle = math.atan2(self.y_collision, self.x_collision)
    
        # Ensure the angle is in the range [0, 2*pi)
        collisionAngle %= (2 * math.pi)
        print(collisionAngle)
    
        # Adjust angle for negative values
        # if self.y_collision < 0 and self.x_collision < 0:
        # collisionAngle += math.pi
        # elif self.x_collision < 0:
        # collisionAngle += math.pi
    
        # Calculate the new position
        new_x = self.x + ((self.radius + (player.rect.width / 2)) * math.cos(collisionAngle)) - (player.rect.width / 2)
        new_y = self.y + ((self.radius + (player.rect.height / 2)) * (-1) * math.sin(collisionAngle) - (player.rect.height / 2))
    
        # Set the player's position
        player.setPos(new_x, new_y)
    
        # Reset player's velocities and accelerations
        player.velocity_x = 0
        player.velocity_y = 0
        player.acceleration_x = 0
        player.acceleration_y = 0
