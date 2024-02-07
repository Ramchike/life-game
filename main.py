import pygame
from config import *

WIDTH = 900
HIGHT = 500

DISPLAY = pygame.display.set_mode((WIDTH, HIGHT))
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

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        DISPLAY.blit(self.image, (self.rect.x, self.rect.y))
        
    def if_hover(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos[0], pos[1])
    
    def if_clicked(self):
        pos = pygame.mouse.get_pos()
        return pygame.mouse.get_pressed()[0] and self.if_hover()
        
        
class DrawUI():
    
    def main_menu():
        DISPLAY.fill(COLOUR["BLACK"])

        title = pygame.image.load(TEXT_MENU).convert_alpha()
        new_game_off = pygame.image.load(BUTTONS_OFF["Создать игру"]).convert_alpha()
        stats_off = pygame.image.load(BUTTONS_OFF["Статистика"]).convert_alpha()
        quit_off = pygame.image.load(BUTTONS_OFF["Выйти"]).convert_alpha()
        new_game_on = pygame.image.load(BUTTONS_ON["Создать игру"]).convert_alpha()
        stats_on = pygame.image.load(BUTTONS_ON["Статистика"]).convert_alpha()
        quit_on = pygame.image.load(BUTTONS_ON["Выйти"]).convert_alpha()

        title_menu = Button(34, 45, title)
        
        new_game_off_button = Button(34, 180, new_game_off)
        stats_off_button = Button(34, 270, stats_off)
        quit_off_button = Button(34, 360, quit_off)
        
        BUTTONS = [new_game_off_button, stats_off_button, quit_off_button]
        
        title_menu.draw()
        new_game_off_button.draw()
        stats_off_button.draw()
        quit_off_button.draw()
        
        # Отрисовка кнопок при наведении на них.
        if new_game_off_button.if_hover():
            new_game_off_button.image = new_game_on
            new_game_off_button.draw()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)            
        elif stats_off_button.if_hover():
            stats_off_button.image = stats_on
            stats_off_button.draw()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif quit_off_button.if_hover():
            quit_off_button.image = quit_on
            quit_off_button.draw()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
        if new_game_off_button.if_clicked():
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            DrawUI.game_screen()
        
        pygame.display.update()

    def game_screen():
        CLICKED = False
        RUN = True
        
        pos = pygame.mouse.get_pos()
        DISPLAY.fill(COLOUR["BLACK"])
        game_menu = pygame.image.load(TEXT_BOARD).convert_alpha()
        back_off = pygame.image.load(BUTTONS_OFF["Назад"]).convert_alpha()
        back_on = pygame.image.load(BUTTONS_ON["Назад"]).convert_alpha()
        
        game_menu_title = Button(244, 26, game_menu)
        back_off_button = Button(24, 454, back_off)
        
        if back_off_button.if_hover():
            back_off_button.image = back_on
            back_off_button.draw()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if back_off_button.if_clicked():
            RUN = False
            
        game_menu_title.draw()
        back_off_button.draw()
        board = Board(BOARD['x'], BOARD['y'], BOARD['width'] + BOARD['x'], BOARD['height'] + BOARD['y'], BOARD['grid'])
        board.draw()
        if board.rect.collidepoint(pos[0], pos[1]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        while RUN:
            pos = pygame.mouse.get_pos()
            board.is_hover()
            if board.rect.collidepoint(pos[0], pos[1]):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if back_off_button.if_hover():
                back_off_button.image = back_on
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                back_off_button.image = back_off
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            back_off_button.draw()
            if back_off_button.if_clicked():
                RUN = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
            pygame.display.update()
        
            
class Board():
    def __init__(self, x, y, width, height, size, random=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = size
        self.cell_w = self.width // self.size
        self.cell_h = self.height // self.size
        self.random = random
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.selected = [[0]*self.cell_w]*self.cell_h
    
    def draw(self):
        pos = pygame.mouse.get_pos()
        for x in range(self.x, self.width, self.size):
            for y in range(self.y, self.height, self.size):
                rect = pygame.Rect(x, y, self.size, self.size)
                pygame.draw.rect(DISPLAY, (199, 199, 199), rect, 1)
                
    def is_hover(self):
        pos = pygame.mouse.get_pos()
        for x in range(self.x, self.width, self.size):
            for y in range(self.y, self.height, self.size):
                rect = pygame.Rect(x, y, self.size, self.size)
                if rect.collidepoint(pos[0], pos[1]):
                    pygame.draw.rect(DISPLAY, (199, 199, 199), rect, 0)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if pygame.mouse.get_pressed()[0]:
                         print(f"PRESSED ON [{x // self.x - 1}] [{y // self.y - 1}]")
                elif self.selected[x // self.x - 1][y // self.y - 1] != 1:
                    pygame.draw.rect(DISPLAY, (0, 0, 0), rect, 0)
                    pygame.draw.rect(DISPLAY, (199, 199, 199), rect, 1)
                    
    
    def is_clicked(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos[0], pos[1]) and pygame.mouse.get_pressed[0]
                    
            
    
game = Game()
game.start()
pygame.quit()



