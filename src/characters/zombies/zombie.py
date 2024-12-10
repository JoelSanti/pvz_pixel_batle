import pygame, random

class Zombie:

    def __init__(self, game, type, lane):
        # Inicializa el zombie con la instancia del juego, tipo y carril
        self.game = game
        self.type = type
        self.lane = lane
        # Establece la posición inicial del zombie
        self.pos = [self.game.screen.get_width(), (lane * self.game.cell_height) + int(self.game.screen.get_height() * 0.24)]

        # Carga la imagen del zombie desde los recursos del juego
        self.img = pygame.transform.scale(game.assets["zombies"][type], (self.game.cell_width, self.game.cell_height))

        # Establece la velocidad y el estado inicial del zombie
        self.speed = 0.35
        self.moving = True

        # Establece la salud inicial del zombie
        self.health = 5
        self.damage = 1  # Añadir esta línea para definir el atributo de daño

    def rect(self):
        # Devuelve el rectángulo que representa la posición y el tamaño del zombie
        return pygame.Rect(self.pos[0], self.pos[1], self.game.cell_width, self.game.cell_height)

    def update(self):
        # Asume que el zombie se está moviendo inicialmente
        self.moving = True
        # Verifica colisiones con plantas en el mismo carril
        for plant in self.game.grid[self.lane]:
            if plant != 0:
                if self.rect().colliderect(plant.rect()):
                    # Deja de moverse si se detecta una colisión y reduce gradualmente la salud de la planta
                    self.moving = False
                    plant.health -= self.damage * 0.005  # Reducir la salud gradualmente
        # Mueve el zombie si no está colisionando con ninguna planta
        if self.moving:
            self.pos[0] -= self.speed

    def draw(self, display):
        # Dibuja el zombie en la pantalla
        display.blit(self.img, (int(self.pos[0]), int(self.pos[1])))

