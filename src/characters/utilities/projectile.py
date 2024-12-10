import pygame

class Projectile:
    """
    Clase que representa un proyectil en el juego.

    Atributos:
        game (Game): Instancia del juego.
        pos (list): Posición del proyectil [x, y].
        speed (list): Velocidad del proyectil [vx, vy].
        damage (int): Daño que causa el proyectil.
        img (Surface): Imagen del proyectil.
    """
    def __init__(self, game, pos, speed, damage):
        """
        Inicializa un nuevo proyectil.

        Args:
            game (Game): Instancia del juego.
            pos (tuple): Posición inicial del proyectil (x, y).
            speed (tuple): Velocidad del proyectil (vx, vy).
            damage (int): Daño que causa el proyectil.
        """
        self.game = game
        self.pos = list(pos) 
        self.speed = list(speed)  
        self.damage = damage
        self.img = pygame.transform.scale(game.assets["projectiles"]["pea"], (game.cell_width // 3, game.cell_height // 3))

    def rect(self):
        """
        Obtiene el rectángulo que representa el área del proyectil.

        Returns:
            Rect: Rectángulo del proyectil.
        """
        return pygame.Rect(self.pos[0], self.pos[1], self.game.cell_width // 3, self.game.cell_height // 3)

    def update(self):
        """
        Actualiza la posición del proyectil según su velocidad.
        """
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    def draw(self, display):
        """
        Dibuja el proyectil en la pantalla.

        Args:
            display (Surface): Superficie donde se dibuja el proyectil.
        """
        display.blit(self.img, (int(self.pos[0]), int(self.pos[1])))