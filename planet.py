import pygame
import sys
import math
import random

def create_multicolored_circle(radius):
    surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

    # Draw the base circle with a random color
    R=random.randint(15, 240)
    B=random.randint(15, 240)
    G=random.randint(15, 240)
    base_color = (R, G, B)
    pygame.draw.circle(surface, base_color, (radius, radius), radius)
    i=0
    while(i<200):
        x=random.randint(-round(radius*7.5/10),round(radius*7.5/10))
        y=random.uniform(-math.sqrt(radius*radius*60/100-x*x),math.sqrt(radius*radius*60/100-x*x))
        j=0
        r=R+random.randint(-15,15)
        b=B+random.randint(-15,15)
        g=G+random.randint(-15,15)
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
    def __init__(self, x, y, radius, resources, mass):
        self.x = x
        self.y = y 
        self.radius = radius
        self.x_collision = 0
        self.y_collision = 0
        self.collisionRadius = 0
        self.centerx = 0
        self.centery = 0
        self.resX=0
        self.resY=0
        self.mass=mass
        self.hasFuel = resources[0]
        self.hasOxygen = resources[1]
        self.hasWater = resources[2]
        self.hasSteel = resources[3]
        self.surface = create_multicolored_circle(radius)
        self.landed = False

    def draw(self,screen, posx,posy,x,y):
        screen.blit(self.surface, ((self.resX/2)+self.x-self.radius-posx-40,(self.resY/2)+self.y-self.radius-posy-40))
        
    def update(self):
        pass

    def getRez(self,resx,resy):
        self.resX=resx
        self.resY=resy
    def retX(self):
        return self.x
    def retY(self):
        return self.y
    def getLanded(self):
        return self.landed
    
    def check_collision(self, player):
        self.centerx = (player.posx + player.rect.width / 2)
        self.centery = (player.posy + player.rect.height / 2)
        distance = ((self.x - self.centerx) ** 2 + (self.y - self.centery) ** 2) ** 0.5
        self.collisionRadius = distance
        if(distance < (self.radius + player.rect.width / 2)):
            self.x_collision = self.centerx - self.x
            self.y_collision= -(self.centery - self.y)
            self.landed = True
            print("Landed")
        else:
            self.landed = False
            print("Not landed")
        return distance < self.radius + player.rect.width / 2

    def handle_collision(self, player):

        collisionAngle = math.atan2(self.y_collision, self.x_collision)
    
        # Ensure the angle is in the range [0, 2*pi)
        collisionAngle %= (2 * math.pi)
    
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
        
        rocketAngle = player.angle % (2 * math.pi)
        if(rocketAngle >= 0.95*collisionAngle and rocketAngle <= 1.05*collisionAngle):
            player.angle = collisionAngle
            player.landed = True
            
            if(self.hasFuel):
                player.gettingFuel = True
            elif(self.landed == False):
                player.gettingFuel = False
                self.hasFuel = False
            else:
                player.gettingFuel = False
                self.hasFuel = False

            if(self.hasOxygen):
                player.gettingOxygen = True
            elif(self.landed == False):
                player.gettingOxygen = False
                self.hasOxygen = False
            else:
                player.gettingOxygen = False
                self.hasOxygen = False

            if(self.hasWater):
                player.gettingWater = True
            elif(self.landed == False):
                player.gettingWater = False
                self.hasWater = False
            else:
                player.gettingWater = False
                self.hasWater = False

            if(self.hasSteel):
                player.gettingSteel = True
            elif(self.landed == False):
                player.gettingSteel = False
                self.hasSteel = False
            else:
                player.gettingSteel = False
                self.hasSteel = False
        