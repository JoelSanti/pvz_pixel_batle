import random
import pygame
from src.characters.utilities.Sun import Sun
from .plant import Plant

class Sunflower(Plant):
    def __init__(self, game, pos):
        super().__init__(game, "sunflower", pos, 8)
        self.cooldown = 120

    def update(self, draw_pos):
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
        if self.cooldown <= 60:
            img_mask = pygame.mask.from_surface(self.img)
            img_mask = img_mask.to_surface()
            img_mask.set_colorkey((0, 0, 0))
            img_mask.set_alpha(30)
            super().draw(display, draw_pos)
            display.blit(img_mask, draw_pos)
        else:
            super().draw(display, draw_pos)
