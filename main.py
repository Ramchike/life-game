import pygame
from screeninfo import get_monitors

m = get_monitors()

class Game():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)