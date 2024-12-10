# src/main.py
import pygame
from src.components import Button
import sys
from src.pages.play import play
from src.pages.options import options

pygame.init()

SCREEN = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Menu")

BG = pygame.image.load('../assets/img/fondo_inicio.png')
BG = pygame.transform.scale(BG, (SCREEN.get_width(), SCREEN.get_height()))

def get_font(size):
    """
    Devuelve una fuente de pygame con el tamaño especificado.
    
    :param size: Tamaño de la fuente.
    :return: Objeto de fuente de pygame.
    """
    return pygame.font.Font("../assets/font.ttf", size)

def main_menu():
    """
    Función principal del menú. Muestra el menú principal y maneja los eventos de los botones.
    """
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("../assets/Play Rect.png"), (int(SCREEN.get_width() * 0.1), int(SCREEN.get_height() * 0.06))), pos=(int(SCREEN.get_width() * 0.85), int(SCREEN.get_height() * 0.4)),
                             text_input="PLAY", font=get_font(int(SCREEN.get_height() * 0.016)), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("../assets/Play Rect.png"), (int(SCREEN.get_width() * 0.1), int(SCREEN.get_height() * 0.06))), pos=(int(SCREEN.get_width() * 0.85), int(SCREEN.get_height() * 0.5)),
                                text_input="OPCIONES", font=get_font(int(SCREEN.get_height() * 0.016)), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("../assets/Play Rect.png"), (int(SCREEN.get_width() * 0.1), int(SCREEN.get_height() * 0.06))), pos=(int(SCREEN.get_width() * 0.85), int(SCREEN.get_height() * 0.65)),
                             text_input="SALIR", font=get_font(int(SCREEN.get_height() * 0.016)), base_color="#d7fcd4", hovering_color="White")

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

# Inicia el menú principal
main_menu()