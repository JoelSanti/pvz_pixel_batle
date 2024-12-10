import random
from src.characters.utilities import Projectile
from .plant import Plant

class Peashooter(Plant):
    def __init__(self, game, pos):
        super().__init__(game, "peashooter", pos, 8)
        self.cooldown = 120

    def update(self, draw_pos):
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
        super().draw(display, draw_pos)