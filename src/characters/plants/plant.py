import pygame, random

class Plant:
    """
    Representa una planta en el juego.

    Atributos:
        game (Game): Instancia del juego.
        type (str): Tipo de planta.
        pos (tuple): Posición de la planta en la cuadrícula.
        max_health (int): Salud máxima de la planta.
        health (int): Salud actual de la planta.
        damage_cooldown (int): Tiempo de espera entre daños.
    """
    def __init__(self, game, type, pos, max_health):
        """
        Inicializa una nueva instancia de Plant.

        Args:
            game (Game): Instancia del juego.
            type (str): Tipo de planta.
            pos (tuple): Posición de la planta en la cuadrícula.
            max_health (int): Salud máxima de la planta.
        """
        self.game = game
        self.type = type
        self.pos = pos
        self.img = game.assets["plants"][type]
        self.max_health = max_health
        self.health = max_health

        self.damage_cooldown = 30

    def rect(self):
        """
        Obtiene el rectángulo de la planta para la detección de colisiones.

        Returns:
            pygame.Rect: Rectángulo de la planta.
        """
        return pygame.Rect((self.pos[0] * 24) + 56, (self.pos[1] * 24) + 50, 16, 16)

    def update(self, draw_pos):
        """
        Actualiza el estado de la planta.

        Args:
            draw_pos (tuple): Posición de dibujo de la planta.
        """
        self.damage_cooldown -= 1

    def draw(self, display, draw_pos):
        """
        Dibuja la planta en la pantalla.

        Args:
            display (pygame.Surface): Superficie en la que se dibuja la planta.
            draw_pos (tuple): Posición de dibujo de la planta.
        """
        display.blit(self.img, draw_pos)

    def damage(self):
        """
        Aplica daño a la planta y reproduce un efecto de sonido.

        Si el tiempo de espera entre daños ha pasado, reduce la salud de la planta
        y reinicia el tiempo de espera.
        """
        if self.damage_cooldown <= 0:
            self.health -= 1
            self.damage_cooldown = 30
            random.choice(self.game.assets["sfx"]["chomp"]).play()
