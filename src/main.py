# src/main.py
import pygame
from src.components.ui.button import Button
import sys
from src.pages.play import play
from src.pages.options import options

pygame.init()

SCREEN = pygame.display.set_mode((1234, 992))
pygame.display.set_caption("Menu")

BG = pygame.image.load('../assets/img/fondo_inicio.png')
BG = pygame.transform.scale(BG, (SCREEN.get_width(), SCREEN.get_height()))
def get_font(size):
    return pygame.font.Font("../assets/font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(1050, 400),
                             text_input="PLAY", font=get_font(16), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(1050, 500),
                                text_input="OPCIONES", font=get_font(16), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(1050, 650),
                             text_input="SALIR", font=get_font(16), base_color="#d7fcd4", hovering_color="White")

        for buttonInicio in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                buttonInicio.changeColor(MENU_MOUSE_POS)
                buttonInicio.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play(SCREEN, get_font)
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options(SCREEN, get_font)
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
main_menu()