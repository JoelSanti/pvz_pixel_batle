import pygame, random

class Plant:
    def __init__(self, game, type, pos, max_health):
        self.game = game
        self.type = type
        self.pos = pos
        self.img = game.assets["plants"][type]
        self.max_health = max_health
        self.health = max_health

        self.damage_cooldown = 30

    def rect(self):
        return pygame.Rect((self.pos[0] * 24) + 56, (self.pos[1] * 24) + 50, 16, 16)

    def update(self, draw_pos):
        self.damage_cooldown -= 1

    def draw(self, display, draw_pos):
        display.blit(self.img, draw_pos)

    def damage(self):
        if self.damage_cooldown <= 0:
            self.health -= 1
            self.damage_cooldown = 30
            random.choice(self.game.assets["sfx"]["chomp"]).play()
