import pygame

class ButtonGame:
    def __init__(self, x, y, width, height, text, bg_image):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.bg_image = pygame.transform.scale(bg_image, (width, height))
        self.text_color = (0, 255, 0)  # Green

    def draw(self, screen):
        screen.blit(self.bg_image, self.rect.topleft)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        text_rect.y -= 5  # Adjust this value to move the text higher
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return self.rect.collidepoint(event.pos)