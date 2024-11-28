import pygame

class ButtonInicio:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.bg_color = (23, 122, 137)  # Darker Turquoise
        self.border_color = (255, 215, 0)  # Gold
        self.text_color = (255, 255, 255)  # WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=10)
        pygame.draw.rect(screen, self.border_color, self.rect, 3, border_radius=10)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return self.rect.collidepoint(event.pos)