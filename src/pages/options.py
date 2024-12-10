import pygame, sys
from src.components.ui.button import Button

def options(SCREEN, get_font):
    volume = 0.5  # Initial volume level
    pygame.mixer.music.set_volume(volume)  # Set initial volume
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(14).render("Apartado de las opciones.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN.get_width() // 2, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Volume control text
        VOLUME_TEXT = get_font(14).render(f"Volumen: {int(volume * 100)}%", True, "Black")
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(SCREEN.get_width() // 2, 360))
        SCREEN.blit(VOLUME_TEXT, VOLUME_RECT)

        # Volume control slider
        VOLUME_SLIDER_RECT = pygame.Rect((SCREEN.get_width() // 2) - 100, 400, 200, 10)
        pygame.draw.rect(SCREEN, "Black", VOLUME_SLIDER_RECT)
        VOLUME_HANDLE_RECT = pygame.Rect((SCREEN.get_width() // 2) - 100 + int(volume * 200) - 5, 395, 10, 20)
        pygame.draw.rect(SCREEN, "Red", VOLUME_HANDLE_RECT)

        OPTIONS_BACK = Button(
            image=None,
            pos=(SCREEN.get_width() // 2, 460),
            text_input="ATRAS",
            font=get_font(14),
            base_color="Red",
            hovering_color="Green",
        )

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return
                if VOLUME_SLIDER_RECT.collidepoint(event.pos):
                    volume = (event.pos[0] - (SCREEN.get_width() // 2 - 100)) / 200
                    volume = max(0, min(volume, 1))  # Clamp the value between 0 and 1
                    pygame.mixer.music.set_volume(volume)  # Update volume

        pygame.display.update()
