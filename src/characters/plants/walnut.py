from .plant import Plant

class Walnut(Plant):
    def __init__(self, game, pos):
        self.game = game
        self.type = "walnut"
        self.pos = pos
        self.max_health = 30
        self.health = 30

        self.img = game.assets["plants"]["walnut"][0]

        self.damage_cooldown = 30

    def update(self, draw_pos):
        if self.health <= 20:
            self.img = self.game.assets["plants"]["walnut"][1]
            if self.health <= 10:
                self.img = self.game.assets["plants"]["walnut"][2]

        return super().update(draw_pos)

    def draw(self, display, draw_pos):
        super().draw(display, draw_pos)
