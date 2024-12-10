import pygame

def initialize_audio():
    """
    Inicializa el sistema de audio y reproduce la música de fondo.

    Carga el archivo de música 'grasswalk.mp3' desde la carpeta de assets,
    lo reproduce en bucle infinito y establece el volumen al 40%.

    Asegúrate de que el archivo de música existe en la ruta especificada.
    """
    pygame.mixer.music.load("../assets/music/grasswalk.mp3")
    pygame.mixer.music.play(-1, 0, 100)
    pygame.mixer.music.set_volume(0.4)