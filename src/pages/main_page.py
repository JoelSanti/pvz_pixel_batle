import pygame
import sys
from src.components.ui.button_inicio import ButtonInicio

def main_page(screen):
    # Cargar la imagen de fondo
    background = pygame.image.load('../assets/img/fondo_inicio.png')
    background = pygame.transform.scale(background, (1234, 992))

    # Crear botones
    button1 = ButtonInicio(990, 400, 150, 50, 'START')
    button2 = ButtonInicio(990, 500, 150, 50, 'OPCIONES')
    button3 = ButtonInicio(990, 650, 150, 50, 'CRÉDITOS')
    button4 = ButtonInicio(990, 740, 150, 50, 'SALIR')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.is_clicked(event):
                    return 'start_game'
                elif button2.is_clicked(event):
                    print("Button 2 clicked")
                elif button3.is_clicked(event):
                    print("Button 3 clicked")
                elif button4.is_clicked(event):
                    pygame.quit()
                    sys.exit()

        screen.blit(background, (0, 0))
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        pygame.display.flip()