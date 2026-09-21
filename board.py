import pygame

class Board:
    def __init__(self):
        self.x = 200
        self.y = 0
        self.square_size = 75
        self.row = None
        self.col = None
        self.is_highlight = False

        self.board = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
        ]

    def draw(self, surface, pieces):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]

                if piece is not None:
                    x = self.x + col * self.square_size
                    y = self.y + row * self.square_size

                    surface.blit(
                        pieces.images[piece],
                        (x, y)
                    )

    def get_square(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        col = (mouse_x - self.x) // self.square_size
        row = (mouse_y - self.y) // self.square_size

        if 0 <= row < 8 and 0 <= col < 8:
            return row, col

        return None

    def set_row_and_col(self, row, col):
        if self.board[row][col] is not None:
            self.row = row
            self.col = col
            self.is_highlight = True

    def clear(self):
        self.row = None
        self.col = None
        self.is_highlight = False

    def highlight_square(self, surface):
        highlight = pygame.Surface(
            (self.square_size, self.square_size),
            pygame.SRCALPHA
        )

        highlight.fill((255, 255, 0, 180))

        x = self.x + self.col * self.square_size
        y = self.y + self.row * self.square_size

        surface.blit(highlight, (x, y))