# src/components/ui/modal.py
import pygame
from src.components.ui.button_game import ButtonGame

def show_modal(screen, button_background):
    MODAL_COLOR = (190, 131, 165)
    WHITE = (255, 255, 255)

    screen_width, screen_height = screen.get_size()
    modal_width, modal_height = 300, 370
    modal_x = (screen_width - modal_width) // 2
    modal_y = (screen_height - modal_height) // 2
    modal_rect = pygame.Rect(modal_x, modal_y, modal_width, modal_height)

    # Draw the border
    border_rect = pygame.Rect(modal_x - 5, modal_y - 5, modal_width + 10, modal_height + 10)
    pygame.draw.rect(screen, (0, 0, 0), border_rect, border_radius=20)

    # Draw the modal
    pygame.draw.rect(screen, MODAL_COLOR, modal_rect, border_radius=20)

    close_button = ButtonGame(modal_x + 50, modal_y + 300, 200, 80, 'Cerrar', button_background)
    back_button = ButtonGame(modal_x + 50, modal_y + 200, 200, 80, 'INICIO', button_background)
    options_button = ButtonGame(modal_x + 50, modal_y + 100, 200, 80, 'OPCIONES', button_background)

    close_button.draw(screen)
    back_button.draw(screen)
    options_button.draw(screen)

    return close_button, back_button, options_button