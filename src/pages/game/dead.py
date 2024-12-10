import pygame, sys

def dead(game, zombie):
    """
    Muestra la pantalla de muerte cuando el jugador pierde el juego.

    Args:
        game: Instancia del juego que contiene todos los recursos y estados del juego.
        zombie: Instancia del zombie que causó la muerte del jugador.
    """
    running = True
    dead_black = pygame.Surface(game.display.get_size())
    dead_black.set_alpha(2)

    dead_text_1 = game.get_font(32).render("LOS ZOMBIES", False, (50, 255, 50))
    dead_text_1_rect = dead_text_1.get_rect()
    dead_text_1_rect.centerx = game.screen.get_width() // 2

    dead_text_2 = game.get_font(32).render("TE COMIERON EL", False, (50, 255, 50))
    dead_text_2_rect = dead_text_2.get_rect()
    dead_text_2_rect.centerx = game.screen.get_width() // 2
    dead_text_2_rect.centery = game.screen.get_height() // 2 - 30

    dead_text_1_rect.bottom = dead_text_2_rect.top

    dead_text_3 = game.get_font(48).render("CEREBRO!", False, (50, 255, 50))
    dead_text_3_rect = dead_text_3.get_rect()
    dead_text_3_rect.centerx = game.screen.get_width() // 2
    dead_text_3_rect.top = dead_text_2_rect.bottom

    game.timer = 0
    pygame.mixer.music.fadeout(100)
    while running:
        game.timer += 1

        game.display.blit(dead_black, (0, 0))
        zombie.draw(game.display)

        if game.timer == 20:
            game.assets["sfx"]["losemusic"].play()
        if game.timer == 240:
            game.assets["sfx"]["chomp"][0].play()
        if game.timer == 280:
            game.assets["sfx"]["chomp"][1].play()
        if game.timer == 300:
            game.assets["sfx"]["losescream"].play()
        if game.timer >= 330:
            game.display.blit(dead_text_1, dead_text_1_rect)
            game.display.blit(dead_text_2, dead_text_2_rect)
            game.display.blit(dead_text_3, dead_text_3_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RETURN:
                    game.run()

        game.screen.blit(pygame.transform.scale(game.display, game.screen.get_size()), (0, 0))
        pygame.display.update()
        game.clock.tick(60)

    pygame.quit()
    sys.exit()