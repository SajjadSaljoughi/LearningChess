import pygame


class Board:
    def __init__(self):
        self.x = 200
        self.y = 0
        self.square_size = 75
        self.row = None
        self.col = None
        self.is_highlight = False
        self.turn = "Player1"

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

    def draw_coordinates(self, surface, font):
        letters = "abcdefgh"

        # Letters: a b c d e f g h
        for col in range(8):
            x = self.x + col * self.square_size + self.square_size // 2
            y = self.y + 8 * self.square_size + 7
            text = font.render(letters[col], True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            surface.blit(text, text_rect)
        # Numbers: 8 7 6 5 4 3 2 1
        for row in range(8):
            x = self.x - 10
            y = self.y + row * self.square_size + self.square_size // 2
            text = font.render(str(8 - row), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            surface.blit(text, text_rect)

    def get_notation(self,row,col):
        letters = "abcdefgh"
        return letters[col] + str(8 - row)

    def move_piece(self, start, end):
        if self.turn == "Player1":
            self.turn = "Player2"
        else:
            self.turn = "Player1"
        start_row, start_col = start
        end_row, end_col = end

        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None

    def attack_piece(self):
        attacks = []
        row = self.row
        col = self.col
        if self.board[row][col] == "wp":
            if self.board[row - 1][col - 1] is not None:
                if self.board[row - 1][col - 1].startswith("b"):
                    attacks.append(((row - 1), (col - 1)))
            if self.board[row - 1][col + 1] is not None:
                if self.board[row - 1][col + 1].startswith("b"):
                    attacks.append(((row - 1), (col + 1)))
        elif self.board[row][col] == "bp":
            if self.board[row + 1][col - 1] is not None:
                if self.board[row + 1][col - 1].startswith("w"):
                    attacks.append(((row + 1), (col - 1)))
            if self.board[row + 1][col + 1] is not None:
                if self.board[row + 1][col + 1].startswith("w"):
                    attacks.append(((row + 1), (col + 1)))
        return attacks

    def get_pawn_moves(self):
        moves = []
        row = self.row
        col = self.col
        # White pawn
        if self.board[row][col] == "wp" and self.turn == "Player1":
            # One square forward
            if row - 1 >= 0 and self.board[row - 1][col] is None:
                moves.append((row - 1, col))

                # Two squares forward on first move
                if row == 6 and self.board[row - 2][col] is None:
                    moves.append((row - 2, col))
        elif self.board[row][col] == "bp" and self.turn == "Player2":
            # One Square forward
            if row + 1 >= 0 and self.board[row + 1][col] is None:
                moves.append((row + 1, col))

                # Two squares forward on first move
                if row == 1 and self.board[row + 2][col] is None:
                    moves.append((row + 2, col))
        return moves

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

    def highlight_available_square(self, surface, row, col, mode="move"):
        if mode == "move":
            highlight = pygame.Surface(
                (self.square_size, self.square_size),
                pygame.SRCALPHA
            )
            highlight.fill((0, 255, 0, 180))
            x = self.x + col * self.square_size
            y = self.y + row * self.square_size
            surface.blit(highlight, (x, y))
        elif mode == "attack":
            highlight = pygame.Surface(
                (self.square_size, self.square_size),
                pygame.SRCALPHA
            )
            highlight.fill((255, 0, 0, 180))
            x = self.x + col * self.square_size
            y = self.y + row * self.square_size
            surface.blit(highlight, (x, y))

    def highlight_square(self, surface):
        highlight = pygame.Surface(
            (self.square_size, self.square_size),
            pygame.SRCALPHA
        )
        highlight.fill((255, 255, 0, 180))
        x = self.x + self.col * self.square_size
        y = self.y + self.row * self.square_size
        surface.blit(highlight, (x, y))
