import random
from src.characters.utilities import Projectile
from .plant import Plant

class Peashooter(Plant):
    """
    Clase que representa un Peashooter, una planta que dispara guisantes a los zombis.
    """
    def __init__(self, game, pos):
        """
        Inicializa un Peashooter.

        :param game: Instancia del juego.
        :param pos: Posición del Peashooter en el jardín.
        """
        super().__init__(game, "peashooter", pos, 8)
        self.cooldown = 120

    def update(self, draw_pos):
        """
        Actualiza el estado del Peashooter, disparando proyectiles si hay zombis en la misma fila.

        :param draw_pos: Posición de dibujo del Peashooter.
        """
        if self.game.zombie_lanes[self.pos[1]]:
            self.cooldown -= random.random() * 2
            if self.cooldown <= 0:
                self.game.projectiles.append(
                    Projectile(
                        self.game,
                        (
                            draw_pos[0] + 20,
                            draw_pos[1] + 80,
                        ),
                        [2, 0],
                        1
                    )
                )
                self.cooldown = 120
                random.choice(self.game.assets["sfx"]["throw"]).play()
        super().update(draw_pos)

    def draw(self, display, draw_pos):
        """
        Dibuja el Peashooter en la pantalla.

        :param display: Superficie donde se dibuja el Peashooter.
        :param draw_pos: Posición de dibujo del Peashooter.
        """
        super().draw(display, draw_pos)