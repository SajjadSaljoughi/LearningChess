import pygame
from color import Color

class Play:
    def __init__(self, w, h, text, name):
        self.text = text
        self.name = name
        self.surface = pygame.Surface((w, h))

    def draw(self):
        self.surface.fill(Color.BLACK)
        return self.surface