import pygame,sys
from pygame import surface

from play import Play

class Button:
    def __init__(self, x, y, w, h, text, name):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.name = name

    def draw(self, surface, mouse_pos , font_btn):
        hovered = self.rect.collidepoint(mouse_pos)
        shadow_rect = self.rect.move(4, 4)
        pygame.draw.rect(surface, (180, 180, 180), shadow_rect, border_radius=10)
        if hovered:
            color = (0, 0, 255)
        else:
            color = (90, 140, 240)
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, (30, 30, 30), self.rect, 2, border_radius=10)
        text_surf = font_btn.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        return hovered

    def execute(self, name):
        if name == "play":
            play_screen = Play(0,0,800,600,"Player VS Player","play")
            play_screen.draw()
            return play_screen.surface
        elif name == "learn":
            ...
        elif name == "quit":
            pygame.quit()
            sys.exit()