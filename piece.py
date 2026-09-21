import pygame


class Piece:
    def __init__(self):
        self.images = {
            "wp": self.load_image("pawn_white.png"),
            "bp": self.load_image("pawn_black.png"),

            "wr": self.load_image("rook_white.png"),
            "br": self.load_image("rook_black.png"),

            "wn": self.load_image("knight_white.png"),
            "bn": self.load_image("knight_black.png"),

            "wb": self.load_image("bishop_white.png"),
            "bb": self.load_image("bishop_black.png"),

            "wq": self.load_image("queen_white.png"),
            "bq": self.load_image("queen_black.png"),

            "wk": self.load_image("king_white.png"),
            "bk": self.load_image("king_black.png"),
        }

    def load_image(self, filename):
        image = pygame.image.load(f"pieces\\{filename}").convert_alpha()
        return pygame.transform.scale(image, (75, 75))
