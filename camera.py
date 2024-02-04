import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # starting point for background
        self.px = -4800
        self.py = -3240

        # space
        image = pygame.image.load('Stars.jpg')
        image = pygame.transform.scale(image, (1920, 1080))
        self.space_surface = image.convert_alpha()
        self.space=pygame.Surface((1920*5,1080*6), pygame.SRCALPHA)
        i=0
        while(i<5):
            j=0
            while(j<6):
                self.space.blit(self.space_surface,(i*1920,j*1080))
                j+=1
            i+=1
        

    def update(self, player):
        self.px += -(player.velocity_x)/10
        self.py += -(player.velocity_y)/10