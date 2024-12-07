import pygame, sys, random
from src.components.ui.button import Button
from src.characters.utilities.Sun import Sun
from src.scripts.utils import Projectile, Particle, ParticleBurst
from src.scripts.plants import Peashooter, Sunflower, Walnut

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
            image=pygame.transform.scale(pygame.image.load("../assets/img/menu_fondo.png"), (120, 60)),
            pos=(1150, 60),
            text_input="SALIR",
            font=self.get_font(16),
            base_color="White",
            hovering_color="Green",
        )
        self.display = screen

        self.assets = {
            "sun": pygame.transform.scale(pygame.image.load("../assets/images/sun.png"), (80, 80)),
            "plants": {
                "peashooter":pygame.transform.scale( pygame.image.load("../assets/images/plants/peashooter.png"), (70, 140)),
                "sunflower": pygame.transform.scale(pygame.image.load("../assets/images/plants/sunflower.png"), (70, 140)),
                "walnut": [pygame.image.load("../assets/images/plants/walnut.png").subsurface((0, 0, 16, 32)),
                           pygame.image.load("../assets/images/plants/walnut.png").subsurface((16, 0, 16, 32)),
                           pygame.image.load("../assets/images/plants/walnut.png").subsurface((32, 0, 16, 32))]
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
        self.cell_width = 24
        self.cell_height = 24
        self.initialize_audio()

    def initialize_audio(self):
        pygame.mixer.music.load("../assets/music/grasswalk.mp3")
        pygame.mixer.music.play(-1, 0, 100)
        pygame.mixer.music.set_volume(0.4)

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
        self.zombie_timer = 600
        self.zombie_max = 1
        self.zombie_max_limit = 10
        self.zombie_last_lane = 5
        self.sun = 150
        self.sun_time = 720
        self.sun_timer = 120
        self.seed_collider_1 = pygame.Rect(140, 40, 90, 120)
        self.seed_collider_2 = pygame.Rect(240, 40, 90, 120)
        self.seed_collider_3 = pygame.Rect(340, 40, 90, 120)

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
                    tile_rect = pygame.Rect((x * 130) + 90, (y * 145) + 210, 130, 145)

                    # Pinta la cuadrícula del juego en forma de ajedréz
                    # pygame.draw.rect(self.display,
                    #               (10 + (10 * ((x + y) % 2)), 10 + (10 * ((x + y) % 2)), 10 + (10 * ((x + y) % 2))),
                    #                tile_rect)

                    if tile != 0:
                        tile.update(((x * 130) + 90 + 30, (y * 145) + 210 - 30))
                        tile.draw(self.display, ((x * 130) + 90 + 30, (y * 145) + 210 - 30))

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
                        self.display.blit(plant_overlay, ((x * 130) + 90 + 30, (y * 145) + 210 - 30))
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
                            plant_center = (tile_rect.centerx, tile_rect.bottom - 50)
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

            self.display.blit(self.assets["seeds"]["walnut"], (140, 40))
            self.display.blit(self.assets["seeds"]["sunflower"], (240, 40))
            self.display.blit(self.assets["seeds"]["peashooter"], (340, 40))



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
                if projectile.life <= 0:
                    self.projectiles.remove(projectile)
                else:
                    projectile.draw(self.screen)

            energy_text = self.get_font(18).render(f"{self.sun}", True, (255, 255, 255))
            self.screen.blit(energy_text, (50, 130))

            self.screen.blit(self.display, (0, 0))
            pygame.display.update()

def play(screen, get_font):
    game = Game(screen, get_font)
    game.run()