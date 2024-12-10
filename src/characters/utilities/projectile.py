import pygame

class Projectile:
    def __init__(self, game, pos, speed, damage):
        self.game = game
        self.pos = list(pos)  # Asegúrate de que pos sea una lista de dos elementos
        self.speed = list(speed)  # Asegúrate de que speed sea una lista de dos elementos
        self.damage = damage
        self.img = pygame.transform.scale(game.assets["projectiles"]["pea"], (game.cell_width // 3, game.cell_height // 3))

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.game.cell_width // 3, self.game.cell_height // 3)

    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    def draw(self, display):
        display.blit(self.img, (int(self.pos[0]), int(self.pos[1])))