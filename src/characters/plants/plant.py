# src/characters/plants/plant.py
import pygame
import time


class Plant:
    def __init__(
        self,
        x,
        y,
        image_path,
        selection_image_path,
        animation_image_path,
        shooting_image_path,
        projectile_image_path=None,
        cost=0,
        recharge_time=0,
        attack_damage=0,
        health=0,
    ):
        self.image = pygame.image.load(image_path)
        self.selection_image = pygame.image.load(selection_image_path)
        self.animation_image = pygame.image.load(animation_image_path)
        self.shooting_image = pygame.image.load(shooting_image_path)
        self.projectile_image = (
            pygame.image.load(projectile_image_path) if projectile_image_path else None
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.cost = cost
        self.recharge_time = recharge_time
        self.attack_damage = attack_damage
        self.health = health
        self.last_planted_time = time.time()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def can_be_planted(self):
        return (time.time() - self.last_planted_time) >= self.recharge_time

    def plant(self):
        if self.can_be_planted():
            self.last_planted_time = time.time()
            return True
        return False
