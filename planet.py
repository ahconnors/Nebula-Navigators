import pygame
import sys
import math
import random
def create_multicolored_circle(radius):
    surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

    # Draw the base circle with a random color
    R=random.randint(10, 245)
    B=random.randint(10, 245)
    G=random.randint(10, 245)
    base_color = (R, G, B)
    pygame.draw.circle(surface, base_color, (radius, radius), radius)
    i=0
    while(i<200):
        x=random.randint(-radius*7.5/10,radius*7.5/10)
        y=random.uniform(-math.sqrt(radius*radius*60/100-x*x),math.sqrt(radius*radius*60/100-x*x))
        j=0
        r=R+random.randint(-20,20)
        b=B+random.randint(-20,20)
        g=G+random.randint(-20,20)
        while(j<20):
            if(x*x+y*y>(radius*radius-radius/10)):
                x+=-x/abs(x)*radius/9
                y+=-y/abs(y)*radius/9
            pygame.draw.circle(surface, (r,g,b), (radius+x, round(y)+radius), radius/10 )
            x+=random.randint(-3,3)
            y+=random.randint(-3,3)
            j+=1
        i+=1
    return surface
class Planet:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_collision = 0
        self.y_collision = 0
        self.collisionRadius = 0
        self.centerx = 0
        self.centery = 0
        self.surface = create_multicolored_circle(radius)

    def draw(self, screen,x,y):
        screen.blit(self.surface, (x-self.radius, y-2*self.radius))

    def update(self):
        pass

    def check_collision(self, player):
        self.centerx = (player.rect.x + player.rect.width / 2)
        self.centery = (player.rect.y + player.rect.height / 2)
        distance = ((self.x - self.centerx) ** 2 + (self.y - self.centery) ** 2) ** 0.5
        self.collisionRadius = distance
        if(distance < (self.radius + player.rect.width / 2)):
            self.x_collision = self.centerx - self.x
            self.y_collision= -(self.centery - self.y)
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