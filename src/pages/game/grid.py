import pygame
import random
from src.characters.plants import Peashooter, Sunflower, Walnut
from src.characters.utilities import ParticleBurst

def initialize_grid():
    """
    Inicializa la cuadrícula del juego con valores predeterminados.

    Returns:
        list: Una lista de listas que representa la cuadrícula del juego, 
              donde cada celda está inicializada con el valor 0.
    """
    return [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

def update_grid(game, tile, tile_rect, play_mouse_pos, x, y):
    """
    Actualiza el estado de una celda específica en la cuadrícula del juego.

    Args:
        game (Game): La instancia del juego.
        tile (Tile): La instancia del objeto en la celda actual.
        tile_rect (Rect): El rectángulo que representa la celda actual.
        play_mouse_pos (tuple): La posición actual del ratón.
        x (int): La coordenada x de la celda en la cuadrícula.
        y (int): La coordenada y de la celda en la cuadrícula.
    """
    if tile != 0:
        tile.update(((x * game.cell_width) + int(game.screen.get_width() * 0.075) + 20, (y * game.cell_height) + int(game.screen.get_height() * 0.24) - 50))
        tile.draw(game.display, ((x * game.cell_width) + int(game.screen.get_width() * 0.075) + 20, (y * game.cell_height) + int(game.screen.get_height() * 0.24) - 50))

        if tile.health <= 0:
            game.grid[y][x] = 0
            game.assets["sfx"]["gulp"].play()

def draw_grid(game, tile, tile_rect, play_mouse_pos, x, y):
    """
    Dibuja la cuadrícula del juego y maneja la lógica de colocación de plantas.

    Args:
        game (Game): La instancia del juego.
        tile (Tile): La instancia del objeto en la celda actual.
        tile_rect (Rect): El rectángulo que representa la celda actual.
        play_mouse_pos (tuple): La posición actual del ratón.
        x (int): La coordenada x de la celda en la cuadrícula.
        y (int): La coordenada y de la celda en la cuadrícula.
    """
    if game.cur_plant != "":
        try:
            plant_overlay = pygame.Surface(game.assets["plants"][game.cur_plant].get_size())
        except:
            plant_overlay = pygame.Surface(game.assets["plants"][game.cur_plant][0].get_size())
        plant_overlay.set_colorkey((0, 0, 0))
        try:
            plant_overlay.blit(game.assets["plants"][game.cur_plant], (0, 0))
        except:
            plant_overlay.blit(game.assets["plants"][game.cur_plant][0], (0, 0))
        game.display.blit(plant_overlay, (play_mouse_pos[0] - 35, play_mouse_pos[1] - 90))

    if tile_rect.collidepoint(play_mouse_pos[0], play_mouse_pos[1]) and tile == 0 and game.cur_plant != "":
        plant_overlay.set_alpha(40)
        game.display.blit(plant_overlay, ((x * game.cell_width) + int(game.screen.get_width() * 0.075) + 20, (y * game.cell_height) + int(game.screen.get_height() * 0.24) - 50))
        if pygame.mouse.get_pressed()[0]:
            if game.cur_plant == "peashooter":
                game.sun -= 100
                game.grid[y][x] = Peashooter(game, [x, y])
                random.choice(game.assets["sfx"]["plant"]).play()
            if game.cur_plant == "sunflower":
                game.sun -= 50
                game.grid[y][x] = Sunflower(game, [x, y])
                random.choice(game.assets["sfx"]["plant"]).play()
            if game.cur_plant == "walnut":
                game.sun -= 50
                game.grid[y][x] = Walnut(game, [x, y])
                random.choice(game.assets["sfx"]["plant"]).play()
            game.cur_plant = ""
            plant_center = (tile_rect.centerx, tile_rect.bottom - 20)
            game.particles += ParticleBurst(
                plant_center, 0.2, 0.1, 270, 20, 10,
                [(115, 23, 45), (20, 160, 46), (26, 122, 62)], 40, 10, 14, 7, True, )
            game.particles += ParticleBurst(
                plant_center, 0.2, 0.1, 90, 20, 10,
                [(115, 23, 45), (20, 160, 46), (26, 122, 62)], 40, 10, 14, 7, True, )