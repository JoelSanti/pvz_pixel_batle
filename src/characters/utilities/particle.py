import pygame, math, random

class Particle:
    """
    Clase que representa una partícula.

    Atributos:
        pos (list): Posición de la partícula.
        vel (list): Velocidad de la partícula.
        life (int): Vida útil de la partícula.
        color (tuple): Color de la partícula.
        size (int): Tamaño de la partícula.
        particle_shrink (bool): Indica si la partícula se encoge con el tiempo.
        gravity (bool): Indica si la gravedad afecta a la partícula.
        y_momentum (float): Momento en el eje y.
        max_life (int): Vida máxima de la partícula.
        max_size (int): Tamaño máximo de la partícula.
    """

    def __init__(
        self, pos, vel, life, color, size=1, particle_shrink=True, gravity=False
    ):
        """
        Inicializa una nueva instancia de la clase Particle.

        Args:
            pos (tuple): Posición inicial de la partícula.
            vel (tuple): Velocidad inicial de la partícula.
            life (int): Vida útil de la partícula.
            color (tuple): Color de la partícula.
            size (int, opcional): Tamaño de la partícula. Por defecto es 1.
            particle_shrink (bool, opcional): Indica si la partícula se encoge con el tiempo. Por defecto es True.
            gravity (bool, opcional): Indica si la gravedad afecta a la partícula. Por defecto es False.
        """
        self.pos = list(pos)
        self.vel = list(vel)
        self.life = life
        self.color = color
        self.size = size
        self.particle_shrink = particle_shrink
        self.gravity = gravity
        self.y_momentum = 0

        self.max_life = self.life
        self.max_size = self.size

    def update(self):
        """
        Actualiza el estado de la partícula.
        """
        self.life -= 1

        if self.gravity:
            self.vel[1] += 0.03

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.particle_shrink:
            self.size = math.ceil((self.life / self.max_life) * self.max_size)

    def draw(self, display):
        """
        Dibuja la partícula en la pantalla.

        Args:
            display (pygame.Surface): Superficie donde se dibuja la partícula.
        """
        pygame.draw.circle(display, self.color, self.pos, self.size)


def ParticleBurst(
    pos,
    speed,
    speed_random,
    angle,
    spread,
    count,
    colors,
    life,
    life_random,
    size,
    size_random,
    particle_shrink=True,
    gravity=False,
):
    """
    Genera una ráfaga de partículas.

    Args:
        pos (tuple): Posición inicial de las partículas.
        speed (float): Velocidad base de las partículas.
        speed_random (float): Variación aleatoria de la velocidad.
        angle (float): Ángulo base de las partículas.
        spread (int): Rango de dispersión del ángulo.
        count (int): Número de partículas a generar.
        colors (list): Lista de colores posibles para las partículas.
        life (int): Vida útil base de las partículas.
        life_random (int): Variación aleatoria de la vida útil.
        size (int): Tamaño base de las partículas.
        size_random (int): Variación aleatoria del tamaño.
        particle_shrink (bool, opcional): Indica si las partículas se encogen con el tiempo. Por defecto es True.
        gravity (bool, opcional): Indica si la gravedad afecta a las partículas. Por defecto es False.

    Returns:
        list: Lista de instancias de la clase Particle.
    """
    particles = []
    for i in range(count):
        angle_random = random.randint(-spread, spread)
        particle_speed = speed + ((random.random() - 0.5) * 2 * speed_random)
        particle_life = life + ((random.random() - 0.5) * 2 * life_random)
        particle_size = size + ((random.random() - 0.5) * 2 * size_random)
        particle_vel = (
            math.sin(math.radians(angle + angle_random)) * particle_speed,
            math.cos(math.radians(angle + angle_random)) * particle_speed,
        )
        particles.append(
            Particle(
                pos,
                particle_vel,
                particle_life,
                random.choice(colors),
                particle_size,
                particle_shrink,
                gravity,
            )
        )
    return particles