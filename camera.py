import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # starting point for rocket
        self.px = 400
        self.py = 300

        # space
        image = pygame.image.load('rainbow.png')
        image = pygame.transform.scale(image, (4000, 3000))
        self.space_surface = image.convert_alpha()
        self.space_rect = self.space_surface.get_rect(topleft = (0,0))

    def cdraw(self, player):
        # calculate scroll
        scrollx = round(player.velocity_x)
        scrolly = round(player.velocity_y)

        # apply scroll to surface
        self.space_surface.scroll(-scrollx, -scrolly)

        # save current position to calculate next scroll
        player.posx = self.px
        player.posy = self.py

        # update surface
        self.display_surface.blit(self.space_surface, self.space_rect)