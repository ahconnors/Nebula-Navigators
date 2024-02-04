import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # starting point for rocket
        self.px = 400
        self.py = 300

        # space
        image = pygame.image.load('Background.png')
        image = pygame.transform.scale(image, (5000, 4000))
        self.space_surface = image.convert_alpha()
        self.space_rect = self.space_surface.get_rect(topleft = (0,0))

    def cdraw(self, player):
        # calculate scroll
        scrollx = player.rect.x - self.px
        scrolly = player.rect.y - self.py

        # apply scroll to surface
        self.space_surface.scroll(-scrollx, -scrolly)

        # save current position to calculate next scroll
        player.rect.x = self.px
        player.rect.y = self.py

        # update surface
        self.display_surface.blit(self.space_surface, [scrollx, scrolly])