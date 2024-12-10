import pygame, math, random

class Sun:
    """
    Clase que representa un objeto Sol en el juego.
    """

    def __init__(self, game, pos, velocity=[0, 0], value=25, life=1200, wave=True):
        """
        Inicializa un nuevo objeto Sol.

        :param game: Instancia del juego.
        :param pos: Posición inicial del Sol.
        :param velocity: Velocidad inicial del Sol.
        :param value: Valor del Sol.
        :param life: Vida útil del Sol.
        :param wave: Indica si el Sol debe moverse en una onda.
        """
        self.game = game
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.value = value
        self.max_life = life
        self.life = life
        self.wave = wave

        self.img = game.assets["sun"]
        print(
            f"Tamaño de la imagen del sol: {self.img.get_size()}"
        ) 

    def rect(self):
        """
        Devuelve el rectángulo que representa la posición y tamaño del Sol.

        :return: Un objeto pygame.Rect.
        """
        return pygame.Rect(self.pos[0], self.pos[1], 80, 80)

    def update(self):
        """
        Actualiza la posición y estado del Sol.
        """
        self.life -= 1

        self.velocity[1] += 0.001
        self.pos[0] += (
            self.velocity[0]
            + (math.sin(math.radians(self.max_life - self.life)) / 3) * self.wave
        )
        self.pos[1] += self.velocity[1]

    def draw(self, display):
        """
        Dibuja el Sol en la pantalla.

        :param display: Superficie en la que se dibuja el Sol.
        """
        display.blit(self.img, (int(self.pos[0]), int(self.pos[1])))
