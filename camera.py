import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_width() / 2
        self.half_height = self.display_surface.get_height() / 2

        # space
        image = pygame.image.load('Background.png')
        image = pygame.transform.scale(image, (5000, 4000))
        self.space_surface = image.convert_alpha()
        self.space_rect = self.space_surface.get_rect(topleft = (0,0))

    def center_on(self, target):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def cdraw(self, player):
        self.center_on(player)

        # space
        space_offset = self.space_rect.topleft - self.offset
        self.display_surface.blit(self.space_surface, space_offset)
