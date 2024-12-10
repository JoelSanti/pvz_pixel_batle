from .plant import Plant

class Walnut(Plant):
    """
    Representa una nuez (Walnut) en el juego.
    
    Atributos:
        game: Referencia al objeto del juego.
        type: Tipo de planta, en este caso "walnut".
        pos: Posición de la nuez en el juego.
        max_health: Salud máxima de la nuez.
        health: Salud actual de la nuez.
        img: Imagen actual de la nuez.
        damage_cooldown: Tiempo de espera entre daños.
    """
    def __init__(self, game, pos):
        """
        Inicializa una instancia de Walnut.
        
        Args:
            game: Referencia al objeto del juego.
            pos: Posición inicial de la nuez.
        """
        self.game = game
        self.type = "walnut"
        self.pos = pos
        self.max_health = 30
        self.health = 30

        self.img = game.assets["plants"]["walnut"][0]

        self.damage_cooldown = 30

    def update(self, draw_pos):
        """
        Actualiza el estado de la nuez, cambiando su imagen según su salud.
        
        Args:
            draw_pos: Posición donde se dibujará la nuez.
        
        Returns:
            Llama al método update de la clase base.
        """
        if self.health <= 20:
            self.img = self.game.assets["plants"]["walnut"][1]
            if self.health <= 10:
                self.img = self.game.assets["plants"]["walnut"][2]

        return super().update(draw_pos)

    def draw(self, display, draw_pos):
        """
        Dibuja la nuez en la pantalla.
        
        Args:
            display: Superficie donde se dibuja la nuez.
            draw_pos: Posición donde se dibujará la nuez.
        """
        super().draw(display, draw_pos)
