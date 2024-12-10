
import pygame, math, random

class Particle:

    def __init__(
        self, pos, vel, life, color, size=1, particle_shrink=True, gravity=False
    ):
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
        self.life -= 1

        if self.gravity:
            self.vel[1] += 0.03

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.particle_shrink:
            self.size = math.ceil((self.life / self.max_life) * self.max_size)

    def draw(self, display):
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