import pygame, sys, random
from src.components.ui.button import Button
from src.characters.utilities.Sun import Sun
class Game:
    def __init__(self, screen, get_font):
        self.screen = screen
        self.get_font = get_font
        self.bg = pygame.image.load('../assets/img/pvz_bg_play.png')
        self.bg = pygame.transform.scale(self.bg, (self.screen.get_width(), self.screen.get_height()))
        # Tiempo en el que un sol tarda en aparecer variable para el contador
        self.sun_timer = 500
        # Tiempo fijo usado como referencia en el que el sol tardará en aparecer
        self.sun_time = 500
        self.projectiles = []
        self.energy = 0
        self.play_back = Button(
            image=pygame.transform.scale(pygame.image.load("../assets/img/menu_fondo.png"), (120, 60)),
            pos=(1150, 60),
            text_input="SALIR",
            font=self.get_font(16),
            base_color="White",
            hovering_color="Green",
        )
        self.assets = {
            "sun": pygame.transform.scale(pygame.image.load("../assets/images/sun.png"), (80, 80))
        }

        self.initialize_audio()
    def initialize_audio(self):
        pygame.mixer.music.load(
            "../assets/music/grasswalk.mp3"
        )
        pygame.mixer.music.play(-1, 0, 100)
        pygame.mixer.music.set_volume(0.4)
    def run(self):
        while True:
            play_mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.bg, (0, 0))
            self.play_back.changeColor(play_mouse_pos)
            self.play_back.update(self.screen)

            self.sun_timer -= 1 + (random.random() - 0.5)
            if self.sun_timer <= 0:
                self.sun_timer = self.sun_time
                self.projectiles.append(Sun(self, [random.randint(0, self.screen.get_width() - 80), -80], [0, 0.2]))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_back.checkForInput(play_mouse_pos):
                        pygame.mixer.music.stop()
                        return
                    for sun in self.projectiles:
                        if sun.rect().collidepoint(event.pos):
                            self.energy += 50
                            self.projectiles.remove(sun)
                            break

            for projectile in self.projectiles:
                projectile.update()
                if projectile.life <= 0:
                    self.projectiles.remove(projectile)
                else:
                    projectile.draw(self.screen)

            energy_text = self.get_font(18).render(f"{self.energy}", True, (255, 255, 255))
            self.screen.blit(energy_text, (50, 130))

            pygame.display.update()

def play(screen, get_font):
    game = Game(screen, get_font)
    game.run()