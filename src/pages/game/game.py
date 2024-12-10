import pygame, sys, random
from src.components.ui.button import Button
from src.characters.utilities import Sun, Projectile, Particle, ParticleBurst
from src.characters.plants import Peashooter, Sunflower, Walnut, Plant
from src.characters.zombies.zombie import Zombie  
from src.pages.game.assets import load_assets
from src.pages.game.audio import initialize_audio
from src.pages.game.dead import dead
from src.pages.game.grid import initialize_grid, update_grid, draw_grid

class Game:
    def __init__(self, screen, get_font):
        self.screen = screen
        self.get_font = get_font
        self.bg = pygame.image.load('../assets/img/pvz_bg_play.png')
        self.bg = pygame.transform.scale(self.bg, (self.screen.get_width(), self.screen.get_height()))
        self.sun_timer = 500
        self.sun_time = 500
        self.projectiles = []
        self.play_back = Button(
            image=pygame.transform.scale(pygame.image.load("../assets/img/menu_fondo.png"), (int(self.screen.get_width() * 0.1), int(self.screen.get_height() * 0.06))),
            pos=(int(self.screen.get_width() * 0.93), int(self.screen.get_height() * 0.06)),
            text_input="SALIR",
            font=self.get_font(int(self.screen.get_height() * 0.016)),
            base_color="White",
            hovering_color="Green",
        )
        self.display = screen
        self.clock = pygame.time.Clock()  
        self.assets = load_assets()
        grid_width = int(self.screen.get_width() * 0.84)  
        grid_height = int(self.screen.get_height() * 0.70)  
        self.cell_width = grid_width // 8  
        self.cell_height = grid_height // 5
        initialize_audio()
        self.zombies = []  
        self.horde_count = 0
        self.zombie_bar_rect = pygame.Rect(self.screen.get_width() - 150, self.screen.get_height() - 30, 140, 20)
        self.zombie_time = 600
        self.zombie_timer = self.zombie_time
        self.horde_delay = 900 
        self.horde_delay_timer = self.horde_delay
        self.zombie_max_limit = 10
        self.zombies_to_add = 2  

    def dead(self, zombie):
        dead(self, zombie)

    def run(self):
        running = True
        self.cur_plant = ""
        self.grid = initialize_grid()
        self.entities = []
        self.particles = []
        self.projectiles = []
        self.zombies = []
        self.zombie_lanes = [False, False, False, False, False]
        self.level_timer = 0
        self.zombie_time = 120
        self.zombie_timer = 120
        self.zombie_max = 1
        self.zombie_max_limit = 10
        self.zombie_last_lane = 5
        self.sun = 150
        self.sun_time = 720
        self.sun_timer = 120
        self.seed_collider_1 = pygame.Rect(int(self.screen.get_width() * 0.11), int(self.screen.get_height() * 0.04), int(self.screen.get_width() * 0.07), int(self.screen.get_height() * 0.12))
        self.seed_collider_2 = pygame.Rect(int(self.screen.get_width() * 0.19), int(self.screen.get_height() * 0.04), int(self.screen.get_width() * 0.07), int(self.screen.get_height() * 0.12))
        self.seed_collider_3 = pygame.Rect(int(self.screen.get_width() * 0.27), int(self.screen.get_height() * 0.04), int(self.screen.get_width() * 0.07), int(self.screen.get_height() * 0.12))
        self.horde_count = 0
        self.horde_delay = 600  # 15 segundos
        self.horde_delay_timer = self.horde_delay
        self.zombie_max_limit = 100
        self.zombies_to_add = 2  # Número inicial de zombies por horda

        while running:
            play_mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.bg, (0, 0))
            self.play_back.changeColor(play_mouse_pos)
            self.play_back.update(self.screen)

            # Generar soles aleatorios
            self.sun_timer -= 1 + (random.random() - 0.5)
            if self.sun_timer <= 0:
                self.sun_timer = self.sun_time
                self.projectiles.append(Sun(self, [random.randint(0, self.screen.get_width() - 80), -80], [0, 0.2]))

            # Actualizar y dibujar la cuadrícula
            y = 0
            for row in self.grid:
                x = 0
                for tile in row:
                    tile_rect = pygame.Rect((x * self.cell_width) + int(self.screen.get_width() * 0.075), (y * self.cell_height) + int(self.screen.get_height() * 0.24), self.cell_width, self.cell_height)
                    update_grid(self, tile, tile_rect, play_mouse_pos, x, y)
                    draw_grid(self, tile, tile_rect, play_mouse_pos, x, y)
                    x += 1
                y += 1

            for i, projectile in sorted(enumerate(self.projectiles), reverse=True):
                projectile.update()
                projectile.draw(self.display)
                if -32 > projectile.pos[0] > 352 or -32 > projectile.pos[1] > 212:
                    self.projectiles.pop(i)
                if isinstance(projectile, Sun):
                    if projectile.rect().collidepoint(play_mouse_pos) and pygame.mouse.get_pressed()[0]:
                        self.projectiles.pop(i)
                        self.sun += projectile.value
                        self.assets["sfx"]["points"].play()
                        self.particles += ParticleBurst(projectile.rect().center, 0.5, 0.3, 0, 180,
                                                        random.randint(10, 14), [(249, 163, 27), (255, 213, 65)], 24, 8,
                                                        3, 1)

            for particle in self.particles:
                particle.update()
                particle.draw(self.display)

            self.display.blit(pygame.transform.scale(self.assets["seeds"]["walnut"], (int(self.screen.get_width() * 0.07), int(self.screen.get_height() * 0.12))), (int(self.screen.get_width() * 0.11), int(self.screen.get_height() * 0.04)))
            self.display.blit(pygame.transform.scale(self.assets["seeds"]["sunflower"], (int(self.screen.get_width() * 0.07), int(self.screen.get_height() * 0.12))), (int(self.screen.get_width() * 0.19), int(self.screen.get_height() * 0.04)))
            self.display.blit(pygame.transform.scale(self.assets["seeds"]["peashooter"], (int(self.screen.get_width() * 0.07), int(self.screen.get_height() * 0.12))), (int(self.screen.get_width() * 0.27), int(self.screen.get_height() * 0.04)))

            # Lógica para añadir hordas de zombis
            if self.horde_delay_timer > 0:
                self.horde_delay_timer -= 1
            else:
                if len(self.zombies) == 0:
                    self.horde_count += 1
                    for _ in range(self.zombies_to_add):
                        lane = random.randint(0, 4)
                        self.zombies.append(Zombie(self, "normal", lane))
                    self.zombies_to_add = min(self.zombies_to_add * 2, self.zombie_max_limit)
                    self.horde_delay_timer = self.horde_delay * (self.horde_count + 1)

            self.entities = self.projectiles + self.zombies

            self.zombie_lanes = [False, False, False, False, False]
            for i, zombie in sorted(enumerate(self.zombies), reverse=True):
                zombie.update()
                zombie.draw(self.display)
                self.zombie_lanes[zombie.lane] = True
                for a, projectile in sorted(enumerate(self.projectiles), reverse=True):
                    if isinstance(projectile, Projectile):
                        if zombie.rect().colliderect(projectile.rect()):
                            zombie.health -= projectile.damage
                            self.projectiles.pop(a)
                            random.choice(self.assets["sfx"]["splat"]).play()
                            self.particles += ParticleBurst(projectile.rect().center, 0.5, 0.3, 0, 180, random.randint(8, 12), [(156,219,67),(89,193,53),(20,160,46)], 16, 8, 2, 1)
                if zombie.health <= 0:
                    self.zombies.pop(i)
                    self.particles += ParticleBurst(zombie.rect().center, 0.7, 0.4, 0, 180, random.randint(24, 32), [(50,132,100),(35,103,78),(115,23,45),(115,23,45),(115,23,45)], 32, 8, 3, 2, True, True)
                if zombie.pos[0] <= 4:
                    self.dead(zombie)
                else:
                    grid_x = int((zombie.pos[0] - int(self.screen.get_width() * 0.075)) // self.cell_width)
                    grid_y = int((zombie.pos[1] - int(self.screen.get_height() * 0.24)) // self.cell_height)
                    if 0 <= grid_x < 8 and 0 <= grid_y < 5:
                        plant = self.grid[grid_y][grid_x]
                        if plant != 0:
                            plant.health -= zombie.damage
                            if plant.health <= 0:
                                self.grid[grid_y][grid_x] = 0
                                self.assets["sfx"]["gulp"].play()

            # Dibujar la barra de progreso de los zombis
            pygame.draw.rect(self.display, (255, 0, 0), self.zombie_bar_rect)
            progress = (self.horde_delay - self.horde_delay_timer) / self.horde_delay
            pygame.draw.rect(self.display, (0, 255, 0), (self.zombie_bar_rect.x, self.zombie_bar_rect.y, int(self.zombie_bar_rect.width * progress), self.zombie_bar_rect.height))

            # Dibujar el contador de hordas
            horde_text = self.get_font(int(self.screen.get_height() * 0.018)).render(f"Horda: {self.horde_count}", True, (255, 255, 255))
            self.display.blit(horde_text, (self.zombie_bar_rect.x, self.zombie_bar_rect.y - 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_back.checkForInput(play_mouse_pos):
                        pygame.mixer.music.stop()
                        return
                    if event.button == 1:
                        if self.seed_collider_1.collidepoint(play_mouse_pos[0], play_mouse_pos[1]):
                            if self.sun >= 50:
                                self.cur_plant = "walnut"
                                self.assets["sfx"]["seedlift"].play()
                            else:
                                self.assets["sfx"]["buzzer"].play()
                        if self.seed_collider_2.collidepoint(play_mouse_pos[0], play_mouse_pos[1]):
                            if self.sun >= 50:
                                self.cur_plant = "sunflower"
                                self.assets["sfx"]["seedlift"].play()
                            else:
                                self.assets["sfx"]["buzzer"].play()
                        if self.seed_collider_3.collidepoint(play_mouse_pos[0], play_mouse_pos[1]):
                            if self.sun >= 100:
                                self.cur_plant = "peashooter"
                                self.assets["sfx"]["seedlift"].play()
                            else:
                                self.assets["sfx"]["buzzer"].play()
                    if event.button == 3:
                        self.cur_plant = ""
                    for sun in self.projectiles:
                        if sun.rect().collidepoint(event.pos):
                            self.sun += 50
                            self.projectiles.remove(sun)
                            break

            for projectile in self.projectiles:
                projectile.update()
                if hasattr(projectile, 'life') and projectile.life <= 0:
                    self.projectiles.remove(projectile)
                else:
                    projectile.draw(self.screen)

            energy_text = self.get_font(int(self.screen.get_height() * 0.018)).render(f"{self.sun}", True, (255, 255, 255))
            self.screen.blit(energy_text, (int(self.screen.get_width() * 0.04), int(self.screen.get_height() * 0.13)))

            self.screen.blit(self.display, (0, 0))
            pygame.display.update()

def play(screen, get_font):
    game = Game(screen, get_font)
    game.run()