# src/main.py
import pygame
from src.pages.main_page import main_page
from src.pages.start_game_page import Game

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1234, 992))
    pygame.display.set_caption("Plants vs. Zombies Clone")

    current_page = 'main'

    while True:
        if current_page == 'main':
            current_page = main_page(screen)
        elif current_page == 'start_game':
            game = Game()
            current_page = game.run()

if __name__ == '__main__':
    run_game()