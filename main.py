import pygame, sys
from color import Color
from button import Button
from play import Play
from piece import Piece
from board import Board

def draw_menu(surface):
    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 400, 400), 4)
    title = font_title.render("Welcome To My App!", True, (0, 0, 0))
    title_rect = title.get_rect(center=(200, 40))
    surface.blit(title, title_rect)

pygame.init()
screen = pygame.display.set_mode((800, 620))
pygame.display.set_caption("Learning Chess With Maizelis")
font_title = pygame.font.SysFont("Times New Roman", 32)
font_btn = pygame.font.SysFont("Arial", 28)
font_coordinates = pygame.font.SysFont("Arial", 18)
font_moves = pygame.font.SysFont("Arial", 20)
background = pygame.image.load("images\\Chess_GameBoard.png").convert()
background = pygame.transform.scale(background, (800, 620))
dark_overlay = pygame.Surface((800, 620))
dark_overlay.set_alpha(120)
dark_overlay.fill((0, 0, 0))
menu_surface = pygame.Surface((400, 400))
menu_surface.fill((255, 255, 255))
buttons = [
    Button(50, 90, 300, 60, "Player VS Player", "play"),
    Button(50, 180, 300, 60, "Learning Book", "learn"),
    Button(50, 270, 300, 60, "Quit", "quit"),
]
current_state = "menu"
play_page = Play(800, 620, "Player VS Player", "play")
return_btn = Button(50, 150, 100, 60, "Return", "return")
pieces = Piece()
board = Board()
available_moves = []
selected_square_piece = None
move_history = []


def draw_move_history(surface, font, move_history):
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

while True:
    mouse_pos = pygame.mouse.get_pos()
    menu_x = mouse_pos[0] - (800 // 2 - 200)
    menu_y = mouse_pos[1] - (620 // 2 - 200)
    menu_mouse_pos = (menu_x, menu_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_state == "menu":
                for btn in buttons:
                    if btn.rect.collidepoint(menu_mouse_pos):
                        if btn.name == "play":
                            current_state = "play"
                        elif btn.name == "learn":
                            current_state = "learn"
                        elif btn.name == "quit":
                            pygame.quit()
                            sys.exit()
            elif current_state == "play":
                menu_x = mouse_pos[0]
                menu_y = mouse_pos[1] - 400
                menu_mouse_pos = (menu_x, menu_y)
                selected_square = board.get_square(mouse_pos)
                if selected_square:
                    row, col = selected_square
                    board.set_row_and_col(row, col)
                    # If a pawn is already selected
                    if board.turn == "Player1":
                        if board.board[row][col]=="wp":
                            available_moves.clear()
                            available_moves = board.get_pawn_moves()
                            selected_square_piece = selected_square
                        if selected_square in available_moves:
                            board.move_piece(selected_square_piece,selected_square)
                            move = board.get_notation(selected_square[0],selected_square[1])
                            move_history.append(move)
                            board.is_highlight = False
                    else:
                        if board.board[row][col]=="bp":
                            available_moves.clear()
                            available_moves = board.get_pawn_moves()
                            selected_square_piece = selected_square
                        if selected_square in available_moves:
                            board.move_piece(selected_square_piece, selected_square)
                            move = board.get_notation(selected_square[0], selected_square[1])
                            move_history.append(move)
                            board.is_highlight = False

                else:
                    board.clear()
                if return_btn.rect.collidepoint(menu_mouse_pos):
                    current_state = "menu"

    if current_state == "menu":
        background = pygame.image.load("images\\Chess_GameBoard.png").convert()
        background = pygame.transform.scale(background, (800, 620))
        screen.blit(background, (0, 0))
        screen.blit(dark_overlay, (0, 0))
        menu_surface.fill((255, 255, 255))
        draw_menu(menu_surface)
        menu_x = mouse_pos[0] - (800//2 - 200)
        menu_y = mouse_pos[1] - (620//2 - 200)
        menu_mouse_pos = (menu_x, menu_y)
        for btn in buttons:
            btn.draw(menu_surface, menu_mouse_pos,font_btn)
        screen.blit(menu_surface, (800//2 - 200, 620//2 - 200))
    elif current_state == "play":
        background = pygame.image.load("images\\New_Chess_GameBoard.png").convert()
        background = pygame.transform.scale(background, (600, 600))
        screen.blit(background, (200, 0))
        side_menu = pygame.Surface((200, 620))
        side_menu.fill((255, 255, 255))
        screen.blit(side_menu, (0, 0))
        coordinate_down = pygame.Surface((800, 20))
        coordinate_down.fill((255, 255, 255))
        screen.blit(coordinate_down, (0, 600))
        menu_x = mouse_pos[0]
        menu_y = mouse_pos[1] - 400
        menu_mouse_pos = (menu_x, menu_y)
        return_btn.draw(side_menu, menu_mouse_pos,font_btn)
        screen.blit(side_menu, (0, 400))
        board.draw_coordinates(screen, font_coordinates)

        for i in range(0, len(move_history), 2):

            move_number = i // 2 + 1

            white_move = move_history[i]

            if i + 1 < len(move_history):
                black_move = move_history[i + 1]
            else:
                black_move = ""

            text = f"{move_number}. {white_move} {black_move}"

            text_surface = font_moves.render(text, True, (0, 0, 0))

            screen.blit(
                text_surface,
                (20, (i // 2) * 30)
            )

        if board.is_highlight:
            board.highlight_square(screen)
            moves = board.get_pawn_moves()
            for row,col in moves:
                board.highlight_available_square(screen, row, col)
            attacks = board.attack_piece()
            for row,col in attacks:
                board.highlight_available_square(screen, row, col, mode="attack")

        board.draw(screen, pieces)
    elif current_state == "learn":
        print("Not implemented yet")
    pygame.display.update()
