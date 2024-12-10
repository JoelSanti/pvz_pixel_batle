
import pygame

def load_assets():
    walnut_image = pygame.image.load("../assets/images/plants/walnut.png")
    walnut_subsurfaces = [
        pygame.transform.scale(walnut_image.subsurface((0, 0, 16, 32)), (70, 140)),
        pygame.transform.scale(walnut_image.subsurface((16, 0, 16, 32)), (70, 140)),
        pygame.transform.scale(walnut_image.subsurface((32, 0, 16, 32)), (70, 140))
    ]

    assets = {
        "sun": pygame.transform.scale(pygame.image.load("../assets/images/sun.png"), (80, 80)),
        "plants": {
            "peashooter": pygame.transform.scale(pygame.image.load("../assets/images/plants/peashooter.png"), (70, 140)),
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
    return assets