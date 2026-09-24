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

    def draw_move_history(self, surface, font, move_history):

        for i in range(0, len(move_history), 2):

            move_number = i // 2 + 1

            white_move = move_history[i]

            if i + 1 < len(move_history):
                black_move = move_history[i + 1]
            else:
                black_move = ""

            text = f"{move_number}. {white_move} {black_move}"

            text_surface = font.render(text, True, (0, 0, 0))

            surface.blit(
                text_surface,
                (20, 180 + (i // 2) * 30)
            )
