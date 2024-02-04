import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # starting point for background
        self.px = 0
        self.py = 0

        # space
        image = pygame.image.load('rainbow.png')
        image = pygame.transform.scale(image, (4000, 3000))
        self.space_surface = image.convert_alpha()
        self.space_rect = self.space_surface.get_rect(topleft = (0,0))

    def update(self, player):
        # calculate scroll
        self.px += -round((player.velocity_x)/10)
        self.py += -round((player.velocity_y)/10)