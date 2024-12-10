
from src.pages.game import Game

def play(screen, get_font):
    game = Game(screen, get_font)
    game.run()