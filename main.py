import pygame
import time
from config import *

WIDTH = 900
HEIGHT = 500

pygame.mixer.init()
pygame.mixer.music.load(MUSIC)

# Подгрузка иконок с конфига в pygame и конвертация их в альфа-канал.
surface = pygame.display.set_mode((WIDTH, HEIGHT))
title_img = pygame.image.load(TEXT_MENU).convert_alpha()
new_game_img = pygame.image.load(BUTTONS["Создать игру"]).convert_alpha()
settings_img = pygame.image.load(BUTTONS["Настройки"]).convert_alpha()
quit_img = pygame.image.load(BUTTONS["Выйти"]).convert_alpha()
game_menu = pygame.image.load(TEXT_BOARD).convert_alpha()
back = pygame.image.load(BUTTONS["Назад"]).convert_alpha()
start = pygame.image.load(BUTTONS["Старт"]).convert_alpha()
ended = pygame.image.load(BUTTONS["Конец игры"]).convert_alpha()


class Button:
    """
    Класс, представляющий кнопку в пользовательском интерфейсе. 
    Он содержит методы для отображения кнопки на экране, проверки нажатия на кнопку.
    """


    def __init__(self, x, y, image, text="", hover_color=(255,255,255)):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.hovered = False
        self.hover_image = self.image.copy()
        
    def draw(self):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
        

class Board:
    """
    Класс, представляющий игровое поле. 
    Он отвечает за отрисовку клеток игрового поля, обработку нажатий на клетки и выполнение логики игры.
    """
    
    
    def __init__(self, x, y, width, height, cell_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_size = cell_size
        
        # Высчет столбцов и строк для матрицы в зависимости от размера поля по ширине и высоте.
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.matrix = [[0]* self.cols for _ in range(self.rows)]
        
    def draw(self, surface=surface):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] == 1:
                    cell_color = (0, 218, 22)
                else:
                    cell_color = (255, 255, 255)
                pygame.draw.rect(surface, cell_color, (self.x + col * self.cell_size, self.y + row * self.cell_size, self.cell_size, self.cell_size), 1 - self.matrix[row][col])

    # Метод для редактирования поля.
    def cell_click (self, pos):
        x, y = pos
        col = (x - self.x) // self.cell_size
        row = (y - self.y) // self.cell_size
        # Проверка на границы матрицы.
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.matrix[row][col] == 1:
                hover_color = (0, 0, 0)
            else:
                hover_color = (0, 90, 9)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
            pygame.draw.rect(surface, hover_color, (self.x + col * self.cell_size, self.y + row * self.cell_size, self.cell_size, self.cell_size), 0)
            # Смена клетки (Живая/Мертвая) при нажатии на неё.
            if pygame.mouse.get_pressed()[0]:
                self.matrix[row][col] = 1 if self.matrix[row][col] == 0 else 0
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.update()


class MainMenu():
    """
    Класс, представляющий главное меню игры. 
    Он содержит методы для отображения главного меню, обработки событий взаимодействия с кнопками меню и перехода к другим частям игры.
    """
    
    
    def __init__(self):
        self.buttons = [
            Button(34, 45, title_img),
            Button(34, 180, new_game_img, "Начать игру"),
            Button(34, 270, settings_img, "Настройки"),
            Button(34, 360, quit_img, "Выйти")
        ]
        self.cursor = pygame.SYSTEM_CURSOR_ARROW
    
    # Метод проверки на события внутри игры.
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.buttons:
                        if button.is_clicked(event.pos):
                            print(button.text)
                            self.handle_button_click(button)
                            
    def is_button_hover(self):
        pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.is_clicked(pos):
                return True
            else:
                return False
                                  
    def handle_button_click(self, button):
        if button.text == "Начать игру":
            game_page = GamePage()
            game_page.construct()
        elif button.text == "Настройки":
            pass
        elif button.text == "Выйти":
            pygame.quit()
            quit()
    
    def draw(self, surface=surface):
        surface.fill((0, 0, 0))
        for button in self.buttons:
            pos = pygame.mouse.get_pos()
            button.draw()
                
        pygame.display.update()

class GamePage:
    """Класс, представляющий игровую страницу. 
    Он отображает игровое поле и кнопки для управления игрой, такие как "Старт" и "Выйти (<)". 
    Также содержит логику обновления игрового поля и проверки условий окончания игры."""
    
    def __init__(self):
        self.buttons = [
            Button(244, 26, game_menu),
            Button(24, 454, back, "Назад"),
            Button(394, 450, start, "Старт")
        ]
        self.game_board = Board(BOARD["x"], BOARD["y"], BOARD["width"], BOARD["height"], BOARD['grid'])
        self.is_started = False
        self.clock = pygame.time.Clock()  # Создание экземпляра объекта Clock
        self.fps = 30  # Частота кадров в секунду

    # Метод проверки на события внутри игры.
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.buttons:
                        if button.is_clicked(event.pos):
                            
                            self.handle_button_click(button)
                            
    def handle_button_click(self, button):
        if button.text == "Назад":
            quit()
        elif button.text == "Старт":
            self.is_started = True
            self.start()
            
    def construct(self):
        while not self.is_started:
            self.handle_events()  # Обработка событий Pygame
            pos = pygame.mouse.get_pos()
            self.draw()  # Отрисовка поля
            self.game_board.cell_click(pos)
                
    def start(self):
        self.is_updating = True
        start_time = time.time()  # Получаем текущее время в секундах
        pygame.mixer.music.play(-1)
        while self.is_updating:
            current_time = time.time()
            self.clock.tick(self.fps)  # Ограничение частоты кадров до self.fps
            self.handle_events()  # Обработка событий Pygame
            self.draw()  # Отрисовка поля
            self.update_game()
            # Проверяем результат игры и останавливаем её.
            if self.game_result(current_time, start_time):  
                self.buttons[0].image = ended
                self.buttons[0].draw()
                pygame.display.update()
                pygame.mixer.music.stop()
                pygame.time.wait(2000)
                break

    def update_game(self):
        """
        Метод обновляет состояние игрового поля с учетом правил игры "Жизнь". 
        Для каждой клетки на игровом поле он использует метод count_live_neighbors, чтобы определить количество живых соседей. 
        Затем, в соответствии с правилами игры, клетка может либо остаться живой, либо умереть, либо стать живой, если ранее была мертвой. 
        Эти изменения записываются в новую сетку (new_grid), 
        которая затем заменяет текущую сетку игры после завершения итерации по всем клеткам поля.
        
        Правила:
        1. Любая живая клетка с менее чем двумя живыми соседями умирает от одиночества.
        2. Любая живая клетка с двумя или тремя живыми соседями продолжает жить на следующее поколение.
        3. Любая живая клетка с более чем тремя живыми соседями умирает от перенаселения.
        4. Любая мертвая клетка с тремя живыми соседями становится живой клеткой от размножения.
        """
        
        
        self.clock.tick(self.fps)  # Ограничение частоты кадров до self.fps
        new_grid = [[0] * self.game_board.cols for _ in range(self.game_board.rows)]
        # Основная логика и правила игры жизнь.
        for row in range(self.game_board.rows):
            for col in range(self.game_board.cols):
                live_neighbors = self.count_live_neighbors(row, col)
                if self.game_board.matrix[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row][col] = 0
                        print("Делаю клетку мертвой")
                    else:
                        new_grid[row][col] = 1
                        print("Делаю клетку живой")
                else:
                    if live_neighbors == 3:
                        new_grid[row][col] = 1
                        print("Делаю клетку живой")
        self.game_board.matrix = new_grid
        print("поменял поле")
        self.draw()
    
    def count_live_neighbors(self, row, col):
        """
        Метод считает количество живых соседей для заданной клетки на игровом поле. 
        Он перебирает все соседние клетки вокруг данной клетки и увеличивает счетчик, если клетка является живой. 
        При этом учитывается, что соседи могут находиться как слева и сверху, так и справа и снизу от выбранной клетки, а также по диагонали.
        """
        
        
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and 0 <= row + i < self.game_board.rows and 0 <= col + j < self.game_board.cols:
                    live_neighbors += self.game_board.matrix[row + i][col + j]
        return live_neighbors
    
    def game_result(self, current_time, start_time):
        if all(cell == 0 for row in self.game_board.matrix for cell in row):
            print("Все клетки вымерли.")
            return True
        elif current_time - start_time >= 30:
            print("Игра застряла в стабильном состоянии. Игра окончена.")
            return True  
        else:
            return False 
        
    def draw(self):
        surface.fill((0, 0, 0))
        self.game_board.draw()
        if not self.is_started:
            for button in self.buttons:
                button.draw()
        pygame.display.update()
            
class Game():
    """
    Основной класс, отвечающий за запуск игры. 
    Он создает экземпляр главного меню и запускает основной игровой цикл.
    """
    
    
    def __init__(self, width=WIDTH, height=HEIGHT, title_window=TITLE_WINDOW):
        self.width = width
        self.height = height
        self.title_window = title_window
    
    def start(self):
        surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title_window)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            main_menu = MainMenu()
            main_menu.draw()
            main_menu.handle_events()
            pygame.display.update()

            
game = Game()
game.start()
pygame.quit()
        
        

