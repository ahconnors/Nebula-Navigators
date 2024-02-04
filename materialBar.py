import pygame

class MaterialBar():
    def __init__(self, x, y, max, color):
        self.x = x
        self.y = y + 100
        self.w = 100
        self.h = 20
        self.max = max
        self.color = color
        self.value = 0
        self.label = ""

    def draw(self, surface):
        ratio = self.value / self.max

        pygame.draw.rect(surface, (100, 100, 100), (self.x, self.y, self.w + 10, self.h + 20))
        pygame.draw.rect(surface, "white", (self.x + 5, self.y + 15, self.w, self.h))
        pygame.draw.rect(surface, self.color, (self.x + 5, self.y + 15, self.w * ratio, self.h))

        font = pygame.freetype.SysFont("Courier", 12, bold=True)
        text, _ = font.render(text=self.label, fgcolor="white")
        surface.blit(text, (self.x + 5, self.y + 5))

    def setValue(self, value):
        if(value < self.max):
            self.value = value
        else:
            self.value = self.max

    def setLabel(self, label):
        self.label = label