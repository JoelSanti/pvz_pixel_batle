import random
import pygame
from src.characters.utilities.Sun import Sun
from .plant import Plant

class Sunflower(Plant):
    """
    Representa una planta girasol que genera soles en el juego.
    """
    def __init__(self, game, pos):
        """
        Inicializa una instancia de Sunflower.

        :param game: Instancia del juego.
        :param pos: Posición inicial de la planta.
        """
        super().__init__(game, "sunflower", pos, 8)
        self.cooldown = 120

    def update(self, draw_pos):
        """
        Actualiza el estado del girasol, generando soles cuando el cooldown llega a cero.

        :param draw_pos: Posición donde se dibuja la planta.
        """
        self.cooldown -= random.random() * 2
        if self.cooldown <= 0:
            self.game.projectiles.append(
                Sun(
                    self.game,
                    [
                        draw_pos[0] + random.randint(-4, 4),
                        draw_pos[1] + 16 + random.randint(-2, 2),
                    ],
                    [0, 0.02],
                    wave=False,
                )
            )
            self.cooldown = 780
        super().update(draw_pos)

    def draw(self, display, draw_pos):
        """
        Dibuja el girasol en la pantalla del juego.

        :param display: Superficie donde se dibuja la planta.
        :param draw_pos: Posición donde se dibuja la planta.
        """
        if self.cooldown <= 60:
            img_mask = pygame.mask.from_surface(self.img)
            img_mask = img_mask.to_surface()
            img_mask.set_colorkey((0, 0, 0))
            img_mask.set_alpha(30)
            super().draw(display, draw_pos)
            display.blit(img_mask, draw_pos)
        else:
            super().draw(display, draw_pos)
