import pygame, sys, random
from src.components.ui.button import Button
from src.characters.utilities import Sun, Projectile, Particle, ParticleBurst
from src.characters.plants import Peashooter, Sunflower, Walnut, Plant
from src.characters.zombies.zombie import Zombie  

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
        self.clock = pygame.time.Clock()  # Inicializar el reloj

        walnut_image = pygame.image.load("../assets/images/plants/walnut.png")
        walnut_subsurfaces = [
        pygame.transform.scale(walnut_image.subsurface((0, 0, 16, 32)), (70, 140)),
        pygame.transform.scale(walnut_image.subsurface((16, 0, 16, 32)), (70, 140)),
        pygame.transform.scale(walnut_image.subsurface((32, 0, 16, 32)), (70, 140))
        ]

        self.assets = {
            "sun": pygame.transform.scale(pygame.image.load("../assets/images/sun.png"), (80, 80)),
            "plants": {
                "peashooter":pygame.transform.scale( pygame.image.load("../assets/images/plants/peashooter.png"), (70, 140)),
                "sunflower": pygame.transform.scale(pygame.image.load("../assets/images/plants/sunflower.png"), (70, 140)),
                "walnut": walnut_subsurfaces
            },
            "seeds": {
                "peashooter": pygame.transform.scale(pygame.image.load("../assets/images/seeds/peashooter.png"), (90, 120)),
                "sunflower": pygame.transform.scale(pygame.image.load("../assets/images/seeds/sunflower.png"), (90, 120)),
                "walnut": pygame.transform.scale(pygame.image.load("../assets/images/seeds/walnut.png"), (90, 120))
            },
            "zombies": {
                "normal": pygame.image.load("../assets/images/zombies/normal.png")
            },
            "projectiles": {
                "pea": pygame.image.load("../assets/images/projectiles/pea.png")
            },
            "sfx": {
                "splat": [pygame.mixer.Sound("../assets/sounds/splat.ogg"),
                          pygame.mixer.Sound("../assets/sounds/splat2.ogg"),
                          pygame.mixer.Sound("../assets/sounds/splat3.ogg")],
                "plant": [pygame.mixer.Sound("../assets/sounds/plant.ogg"),
                          pygame.mixer.Sound("../assets/sounds/plant2.ogg")],
                "gulp": pygame.mixer.Sound("../assets/sounds/gulp.ogg"),
                "swing": pygame.mixer.Sound("../assets/sounds/swing.ogg"),
                "shoop": pygame.mixer.Sound("../assets/sounds/shoop.ogg"),
                "chomp": [pygame.mixer.Sound("../assets/sounds/chomp.ogg"),
                          pygame.mixer.Sound("../assets/sounds/chomp2.ogg")],
                "throw": [pygame.mixer.Sound("../assets/sounds/throw.ogg"),
                          pygame.mixer.Sound("../assets/sounds/throw2.ogg")],
                "losemusic": pygame.mixer.Sound("../assets/sounds/losemusic.ogg"),
                "losescream": pygame.mixer.Sound("../assets/sounds/scream.ogg"),
                "seedlift": pygame.mixer.Sound("../assets/sounds/seedlift.ogg"),
                "buzzer": pygame.mixer.Sound("../assets/sounds/buzzer.ogg"),
                "points": pygame.mixer.Sound("../assets/sounds/points.ogg")
            }
        }
        grid_width = int(self.screen.get_width() * 0.84)  # Adjust grid width as needed
        grid_height = int(self.screen.get_height() * 0.70)  # Adjust grid height as needed
        self.cell_width = grid_width // 8  # Adjusted to fit zombies
        self.cell_height = grid_height // 5
        self.initialize_audio()
        self.zombies = []  # Initialize the list of zombies
        self.horde_count = 0
        self.zombie_bar_rect = pygame.Rect(self.screen.get_width() - 150, self.screen.get_height() - 30, 140, 20)
        self.zombie_time = 600
        self.zombie_timer = self.zombie_time
        self.horde_delay = 900  # 15 segundos
        self.horde_delay_timer = self.horde_delay
        self.zombie_max_limit = 10
        self.zombies_to_add = 2  # Número inicial de zombies por horda

    def initialize_audio(self):
        pygame.mixer.music.load("../assets/music/grasswalk.mp3")
        pygame.mixer.music.play(-1, 0, 100)
        pygame.mixer.music.set_volume(0.4)

    def dead(self, zombie):
        running = True
        dead_black = pygame.Surface(self.display.get_size())
        dead_black.set_alpha(2)

        dead_text_1 = self.get_font(32).render("LOS ZOMBIES", False, (50, 255, 50))
        dead_text_1_rect = dead_text_1.get_rect()
        dead_text_1_rect.centerx = self.screen.get_width() // 2

        dead_text_2 = self.get_font(32).render("TE COMIERON EL", False, (50, 255, 50))
        dead_text_2_rect = dead_text_2.get_rect()
        dead_text_2_rect.centerx = self.screen.get_width() // 2
        dead_text_2_rect.centery = self.screen.get_height() // 2 - 30

        dead_text_1_rect.bottom = dead_text_2_rect.top

        dead_text_3 = self.get_font(48).render("CEREBRO!", False, (50, 255, 50))
        dead_text_3_rect = dead_text_3.get_rect()
        dead_text_3_rect.centerx = self.screen.get_width() // 2
        dead_text_3_rect.top = dead_text_2_rect.bottom

        self.timer = 0
        pygame.mixer.music.fadeout(100)
        while running:
            self.timer += 1

            self.display.blit(dead_black, (0, 0))
            zombie.draw(self.display)

            if self.timer == 20:
                self.assets["sfx"]["losemusic"].play()
            if self.timer == 240:
                self.assets["sfx"]["chomp"][0].play()
            if self.timer == 280:
                self.assets["sfx"]["chomp"][1].play()
            if self.timer == 300:
                self.assets["sfx"]["losescream"].play()
            if self.timer >= 330:
                self.display.blit(dead_text_1, dead_text_1_rect)
                self.display.blit(dead_text_2, dead_text_2_rect)
                self.display.blit(dead_text_3, dead_text_3_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        self.run()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def run(self):
        running = True
        self.cur_plant = ""
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.entities = []
        self.particles = []
        self.projectiles = []
        self.zombies = []
        self.zombie_lanes = [False, False, False, False, False]
        self.level_timer = 0
        self.zombie_time = 600
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
        self.horde_delay = 900  # 15 segundos
        self.horde_delay_timer = self.horde_delay
        self.zombie_max_limit = 10
        self.zombies_to_add = 2  # Número inicial de zombies por horda

        while running:
            play_mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.bg, (0, 0))
            self.play_back.changeColor(play_mouse_pos)
            self.play_back.update(self.screen)

            self.sun_timer -= 1 + (random.random() - 0.5)
            if self.sun_timer <= 0:
                self.sun_timer = self.sun_time
                self.projectiles.append(Sun(self, [random.randint(0, self.screen.get_width() - 80), -80], [0, 0.2]))

            y = 0
            for row in self.grid:
                x = 0
                for tile in row:
                    tile_rect = pygame.Rect((x * self.cell_width) + int(self.screen.get_width() * 0.075), (y * self.cell_height) + int(self.screen.get_height() * 0.24), self.cell_width, self.cell_height)

                    # Pinta la cuadrícula del juego en forma de ajedréz
                    # color = (10 + (10 * ((x + y) % 2)), 10 + (10 * ((x + y) % 2)), 10 + (10 * ((x + y) % 2)))
                    # pygame.draw.rect(self.display, color, tile_rect)

                    if tile != 0:
                        tile.update(((x * self.cell_width) + int(self.screen.get_width() * 0.075) + 20, (y * self.cell_height) + int(self.screen.get_height() * 0.24) - 50))
                        tile.draw(self.display, ((x * self.cell_width) + int(self.screen.get_width() * 0.075) + 20, (y * self.cell_height) + int(self.screen.get_height() * 0.24) - 50))

                        if tile.health <= 0:
                            self.grid[y][x] = 0
                            self.assets["sfx"]["gulp"].play()

                    if self.cur_plant != "":
                        try:
                            plant_overlay = pygame.Surface(self.assets["plants"][self.cur_plant].get_size())
                        except:
                            plant_overlay = pygame.Surface(self.assets["plants"][self.cur_plant][0].get_size())
                        plant_overlay.set_colorkey((0, 0, 0))
                        try:
                            plant_overlay.blit(self.assets["plants"][self.cur_plant], (0, 0))
                        except:
                            plant_overlay.blit(self.assets["plants"][self.cur_plant][0], (0, 0))
                        self.display.blit(plant_overlay, (play_mouse_pos[0] - 35, play_mouse_pos[1] - 90))

                    if tile_rect.collidepoint(play_mouse_pos[0], play_mouse_pos[1]) and tile == 0 and self.cur_plant != "":
                        plant_overlay.set_alpha(40)
                        self.display.blit(plant_overlay, ((x * self.cell_width) + int(self.screen.get_width() * 0.075) + 20, (y * self.cell_height) + int(self.screen.get_height() * 0.24) - 50))
                        if pygame.mouse.get_pressed()[0]:
                            if self.cur_plant == "peashooter":
                                self.sun -= 100
                                self.grid[y][x] = Peashooter(self, [x, y])
                                random.choice(self.assets["sfx"]["plant"]).play()
                            if self.cur_plant == "sunflower":
                                self.sun -= 50
                                self.grid[y][x] = Sunflower(self, [x, y])
                                random.choice(self.assets["sfx"]["plant"]).play()
                            if self.cur_plant == "walnut":
                                self.sun -= 50
                                self.grid[y][x] = Walnut(self, [x, y])
                                random.choice(self.assets["sfx"]["plant"]).play()
                            self.cur_plant = ""
                            plant_center = (tile_rect.centerx, tile_rect.bottom - 20)
                            self.particles += ParticleBurst(
                                plant_center, 0.2, 0.1, 270, 20, 10,
                                [(115, 23, 45), (20, 160, 46), (26, 122, 62)], 40, 10, 14, 7, True, )
                            self.particles += ParticleBurst(
                                plant_center, 0.2, 0.1, 90, 20, 10,
                                [(115, 23, 45), (20, 160, 46), (26, 122, 62)], 40, 10, 14, 7, True, )
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