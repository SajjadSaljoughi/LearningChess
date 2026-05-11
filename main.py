import pygame, sys
from color import Color
from button import Button

def draw_menu(surface):
    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 400, 400), 4, border_radius=12)
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
    Button(50, 90, 300, 60, "Play 2 Players"),
    Button(50, 180, 300, 60, "Learning Book"),
    Button(50, 270, 300, 60, "Quit"),
]

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     for btn in buttons:
        #         if btn.rect.collidepoint((mouse_pos[0] - 200 + 400//2, mouse_pos[1] - 200 + 400//2)):
        #             print(btn.text)
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
    pygame.display.update()
