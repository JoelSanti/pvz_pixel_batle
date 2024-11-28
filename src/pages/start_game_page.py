# src/pages/start_game_page.py
import pygame
import sys
import os
from src.components.ui.button_game import ButtonGame
from src.components.ui.modal_menu import show_modal

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((1234, 992))
        self.background = pygame.image.load(
            os.path.join(os.path.dirname(__file__), '../../assets/img/pvz_background_play.png'))
        self.background = pygame.transform.scale(self.background, (1234, 992))

        self.button_background = pygame.image.load(
            os.path.join(os.path.dirname(__file__), '../../assets/img/menu_fondo.png'))
        self.menu_button = ButtonGame(1044, 20, 150, 80, 'MENÚ', self.button_background)
        self.showing_modal = False

        self.initialize_game_state()
        self.initialize_audio()
        self.initialize_colliders()
        self.initialize_modal_buttons()

        self.assets = {
            "plants": {
                "peashooter": pygame.image.load(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/images/plants/peashooter.png"),
                "sunflower": pygame.image.load(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/images/plants/sunflower.png"),
                "walnut": [pygame.image.load(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/images/plants/walnut.png").subsurface(
                    (0, 0, 16, 32)),
                           pygame.image.load(
                               "../../../PycharmProjects/pvz_pixel_batle/src/data/images/plants/walnut.png").subsurface(
                               (16, 0, 16, 32)),
                           pygame.image.load(
                               "../../../PycharmProjects/pvz_pixel_batle/src/data/images/plants/walnut.png").subsurface(
                               (32, 0, 16, 32))]
            },
            "seeds": {
                "peashooter": pygame.image.load(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/images/seeds/peashooter.png"),
                "sunflower": pygame.image.load(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/images/seeds/sunflower.png"),
                "walnut": pygame.image.load("../../../PycharmProjects/pvz_pixel_batle/src/data/images/seeds/walnut.png")
            },
            "zombies": {
                "normal": pygame.image.load(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/images/zombies/normal.png")
            },
            "projectiles": {
                "pea": pygame.image.load("../../../PycharmProjects/pvz_pixel_batle/src/data/images/projectiles/pea.png")
            },
            "sun": pygame.image.load("../../../PycharmProjects/pvz_pixel_batle/src/data/images/sun.png"),
            "sfx": {
                "splat": [pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/splat.ogg"),
                          pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/splat2.ogg"),
                          pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/splat3.ogg")],
                "plant": [pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/plant.ogg"),
                          pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/plant2.ogg")],
                "gulp": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/gulp.ogg"),
                "swing": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/swing.ogg"),
                "shoop": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/shoop.ogg"),
                "chomp": [pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/chomp.ogg"),
                          pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/chomp2.ogg")],
                "throw": [pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/throw.ogg"),
                          pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/throw2.ogg")],
                "losemusic": pygame.mixer.Sound(
                    "../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/losemusic.ogg"),
                "losescream": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/scream.ogg"),
                "seedlift": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/seedlift.ogg"),
                "buzzer": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/buzzer.ogg"),
                "points": pygame.mixer.Sound("../../../PycharmProjects/pvz_pixel_batle/src/data/sounds/points.ogg")
            }
        }

        self.font16 = pygame.font.Font("../../../PycharmProjects/pvz_pixel_batle/src/data/m6x11.ttf", 16)
        self.font32 = pygame.font.Font("../../../PycharmProjects/pvz_pixel_batle/src/data/m6x11.ttf", 32)
        self.font48 = pygame.font.Font("../../../PycharmProjects/pvz_pixel_batle/src/data/m6x11.ttf", 48)

    def initialize_game_state(self):
        self.cur_plant = ""
        self.mouse_pos = (0, 0)
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]]
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

    def initialize_audio(self):
        pygame.mixer.music.load("../../../PycharmProjects/pvz_pixel_batle/src/data/music/grasswalk.mp3")
        pygame.mixer.music.play(-1, 0, 100)
        pygame.mixer.music.set_volume(0.4)

    def initialize_colliders(self):
        self.seed_collider_1 = pygame.Rect(292, 4, 24, 32)
        self.seed_collider_2 = pygame.Rect(264, 4, 24, 32)
        self.seed_collider_3 = pygame.Rect(236, 4, 24, 32)

    def initialize_modal_buttons(self):
        screen_width, screen_height = self.screen.get_size()
        modal_width, modal_height = 300, 370
        modal_x = (screen_width - modal_width) // 2
        modal_y = (screen_height - modal_height) // 2

        self.close_button = ButtonGame(modal_x + 50, modal_y + 300, 200, 80, 'Cerrar', self.button_background)
        self.back_button = ButtonGame(modal_x + 50, modal_y + 200, 200, 80, 'INICIO', self.button_background)
        self.options_button = ButtonGame(modal_x + 50, modal_y + 100, 200, 80, 'OPCIONES', self.button_background)

    def run(self):
        running = True

        self.display.fill((0, 0, 0))

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = (
            self.mouse_pos[0] * (320 / self.window_size[0]), self.mouse_pos[1] * (180 / self.window_size[1]))


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu_button.is_clicked(event):
                        self.showing_modal = not self.showing_modal
                    elif self.showing_modal:
                        if self.close_button.is_clicked(event):
                            self.showing_modal = False
                        elif self.back_button.is_clicked(event):
                            running = False
                            return 'main'
                        elif self.options_button.is_clicked(event):
                            print("Opciones clicked")

            self.screen.blit(self.background, (0, 0))
            self.menu_button.draw(self.screen)

            if self.showing_modal:
                show_modal(self.screen, self.button_background)
                self.close_button.draw(self.screen)
                self.back_button.draw(self.screen)
                self.options_button.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()