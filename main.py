import pygame
from config import *

DISPLAY = pygame.display.set_mode((900, 500))
pygame.display.set_caption(TITLE_WINDOW)

class Game():

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()

        RUN = True   
        while RUN:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False

            DrawUI.main_menu()
            pygame.display.update()

        pygame.quit()

class Element_UI():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        DISPLAY.blit(self.image, (self.rect.x, self.rect.y))


class DrawUI():
    
    def main_menu():
        DISPLAY.fill(COLOUR["BLACK"])

        title = pygame.image.load(TITLE_MENU).convert_alpha()
        new_game_off = pygame.image.load(BUTTONS_OFF["Создать игру"]).convert_alpha()
        stats_off = pygame.image.load(BUTTONS_OFF["Статистика"]).convert_alpha()
        quit_off = pygame.image.load(BUTTONS_OFF["Выйти"]).convert_alpha()

        title_menu = Element_UI(34, 45, title).draw()
        new_game_off_button = Element_UI(34, 180, new_game_off).draw()
        stats_off_button = Element_UI(34, 270, stats_off).draw()
        quit_off_button = Element_UI(34, 360, quit_off).draw()
        
        pygame.display.update()

        

game = Game()
game.start()
pygame.quit()



