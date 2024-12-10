import pygame, random

class Zombie:
    """
    Clase que representa un zombie en el juego.
    """

    def __init__(self, game, type, lane):
        """
        Inicializa un nuevo zombie.

        :param game: Instancia del juego.
        :param type: Tipo de zombie.
        :param lane: Carril en el que se encuentra el zombie.
        """
        self.game = game
        self.type = type
        self.lane = lane
   
        self.pos = [self.game.screen.get_width(), (lane * self.game.cell_height) + int(self.game.screen.get_height() * 0.24)]

 
        self.img = pygame.transform.scale(game.assets["zombies"][type], (self.game.cell_width, self.game.cell_height))


        self.speed = 0.13  # Velocidad de movimiento del zombie
        self.moving = True  # Indica si el zombie se está moviendo
        self.health = 10  # Salud del zombie
        self.damage = 1  # Daño que el zombie inflige a las plantas

    def rect(self):
        """
        Devuelve el rectángulo que representa la posición y tamaño del zombie.

        :return: pygame.Rect
        """
        return pygame.Rect(self.pos[0], self.pos[1], self.game.cell_width, self.game.cell_height)

    def update(self):
        """
        Actualiza la posición y estado del zombie.
        """
        self.moving = True

        for plant in self.game.grid[self.lane]:
            if plant != 0:
                if self.rect().colliderect(plant.rect()):
                    plant.health -= self.damage
                    self.moving = False  # Detener el movimiento cuando está comiendo una planta
                    break  # Salir del bucle una vez que se encuentra una planta

        if self.moving:
            self.pos[0] -= self.speed

    def draw(self, display):
        """
        Dibuja el zombie en la pantalla.

        :param display: Superficie en la que se dibuja el zombie.
        """
        display.blit(self.img, (int(self.pos[0]), int(self.pos[1])))

