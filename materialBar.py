import pygame

class MaterialBar():
    def __init__(self, x, y, w, h, max, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max = max
        self.color = color
        self.value = 0

    def draw(self, surface):
        ratio = self.value / self.max
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w * ratio, self.h))

    def setValue(self, value):
        self.value = value