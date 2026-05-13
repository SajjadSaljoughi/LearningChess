import pygame, sys
from color import Color
from button import Button
from play import Play
from piece import Piece

def draw_menu(surface):
    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 400, 400), 4)
    title = font_title.render("Welcome To My App!", True, (0, 0, 0))
    title_rect = title.get_rect(center=(200, 40))
    surface.blit(title, title_rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Learning Chess With Maizelis")
font_title = pygame.font.SysFont("Times New Roman", 32)
font_btn = pygame.font.SysFont("Arial", 28)
background = pygame.image.load("images\\Chess_GameBoard.png").convert()
background = pygame.transform.scale(background, (800, 600))
dark_overlay = pygame.Surface((800, 600))
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
play_page = Play(800, 600, "Player VS Player", "play")
return_btn = Button(50, 90, 100, 60, "Return", "return")

while True:
    mouse_pos = pygame.mouse.get_pos()
    menu_x = mouse_pos[0] - (800 // 2 - 200)
    menu_y = mouse_pos[1] - (600 // 2 - 200)
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
                if return_btn.rect.collidepoint(menu_mouse_pos):
                    current_state = "menu"

    if current_state == "menu":
        background = pygame.image.load("images\\Chess_GameBoard.png").convert()
        background = pygame.transform.scale(background, (800, 600))
        screen.blit(background, (0, 0))
        screen.blit(dark_overlay, (0, 0))
        menu_surface.fill((255, 255, 255))
        draw_menu(menu_surface)
        menu_x = mouse_pos[0] - (800//2 - 200)
        menu_y = mouse_pos[1] - (600//2 - 200)
        menu_mouse_pos = (menu_x, menu_y)
        for btn in buttons:
            btn.draw(menu_surface, menu_mouse_pos,font_btn)
        screen.blit(menu_surface, (800//2 - 200, 600//2 - 200))
    elif current_state == "play":
        background = pygame.image.load("images\\Chess_GameBoard.png").convert()
        background = pygame.transform.scale(background, (600, 600))
        screen.blit(background, (200, 0))
        screen.blit(dark_overlay, (200, 0))
        side_menu = pygame.Surface((200, 600))
        side_menu.fill((255, 255, 255))
        screen.blit(side_menu, (0, 0))
        menu_x = mouse_pos[0]
        menu_y = mouse_pos[1] - 400
        menu_mouse_pos = (menu_x, menu_y)
        return_btn.draw(side_menu, menu_mouse_pos,font_btn)
        screen.blit(side_menu, (0, 400))
        pieces = Piece()
        screen.blit(pieces.scaled_pawn_white_image, (200, 460))
        screen.blit(pieces.scaled_pawn_white_image, (275, 460))
        screen.blit(pieces.scaled_pawn_white_image, (350, 460))
        screen.blit(pieces.scaled_pawn_white_image, (425, 460))
        screen.blit(pieces.scaled_pawn_white_image, (500, 460))
        screen.blit(pieces.scaled_pawn_white_image, (575, 460))
        screen.blit(pieces.scaled_pawn_white_image, (650, 460))
        screen.blit(pieces.scaled_pawn_white_image, (725, 460))
        #----------------------------------------------------------------
        screen.blit(pieces.scaled_pawn_black_image, (200, 75))
        screen.blit(pieces.scaled_pawn_black_image, (275, 75))
        screen.blit(pieces.scaled_pawn_black_image, (350, 75))
        screen.blit(pieces.scaled_pawn_black_image, (425, 75))
        screen.blit(pieces.scaled_pawn_black_image, (500, 75))
        screen.blit(pieces.scaled_pawn_black_image, (575, 75))
        screen.blit(pieces.scaled_pawn_black_image, (650, 75))
        screen.blit(pieces.scaled_pawn_black_image, (725, 75))
    elif current_state == "learn":
        ...
    pygame.display.update()
