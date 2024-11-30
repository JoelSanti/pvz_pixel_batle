import pygame, math, random


class Sun:

    def __init__(self, game, pos, velocity=[0, 0], value=25, life=1200, wave=True):
        self.game = game
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.value = value
        self.max_life = life
        self.life = life
        self.wave = wave

        # Usa la imagen del sol escalada desde los assets del juego
        self.img = game.assets["sun"]
        print(
            f"Tamaño de la imagen del sol: {self.img.get_size()}"
        )  # Imprime el tamaño de la imagen escalada

    def rect(self):
        # Ajusta el rectángulo de colisión a un tamaño fijo
        return pygame.Rect(self.pos[0], self.pos[1], 80, 80)

    def update(self):
        self.life -= 1
        self.pos[0] += (
            self.velocity[0]
            + (math.sin(math.radians(self.max_life - self.life)) / 3) * self.wave
        )
        self.pos[1] += self.velocity[1]

    def draw(self, display):
        display.blit(self.img, (int(self.pos[0]), int(self.pos[1])))
