import pygame

class Piece():
    def __init__(self):
        self.pawn_white_image = pygame.image.load("images\\pawn_white.png")
        self.pawn_black_image = pygame.image.load("images\\pawn_black.png")
        self.scaled_pawn_white_image = pygame.transform.scale(self.pawn_white_image, (64, 64))
        self.scaled_pawn_black_image = pygame.transform.scale(self.pawn_black_image, (64, 64))

    def draw(self, surface):
        pygame.draw.rect(surface, (180, 180, 180))