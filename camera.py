import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # starting point for background
        self.px = 0
        self.py = 0

        # space
        image = pygame.image.load('Stars.jpg')
        image = pygame.transform.scale(image, (1920, 1080))
        self.space_surface = image.convert_alpha()
        self.space=pygame.Surface((1920*4,1080*4), pygame.SRCALPHA)
        i=0
        while(i<4):
            j=0
            while(j<4):
                self.space.blit(self.space_surface,(i*1920,j*1080))
                j+=1
            i+=1
        

    def update(self, player):
        self.px += -(player.velocity_x)/10
        self.py += -(player.velocity_y)/10