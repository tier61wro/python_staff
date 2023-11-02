import pygame

# Инициализация Pygame
pygame.init()
info = pygame.display.Info()
WINDOW_WIDTH,  WINDOW_HEIGHT = info.current_w, info.current_h

# Установка размеров окна
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
print(f'{WINDOW_SIZE=}')
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Игровое поле')

# Задание цветов
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Размеры ячейки сетки
CELL_WIDTH = 25
CELL_HEIGHT = 25

# Расчет количества ячеек сетки
GRID_WIDTH = WINDOW_WIDTH // CELL_WIDTH
GRID_HEIGHT = WINDOW_HEIGHT // CELL_HEIGHT

# Создание сетки
grid = []
for i in range(GRID_HEIGHT):
    row = []
    for j in range(GRID_WIDTH):
        rect = pygame.Rect(j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
        row.append(rect)
    grid.append(row)

# Создание фигуры солдатика
soldier_red_rect = pygame.Rect(0, 0, CELL_WIDTH, CELL_HEIGHT)
soldier_red_rect.center = grid[0][0].center
soldier_red_color = RED


soldier_blue_rect = pygame.Rect(0, 0, CELL_WIDTH, CELL_HEIGHT)
soldier_blue_rect.center = grid[0][1].center
soldier_blue_color = BLUE



# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                soldier_red_rect.move_ip(-CELL_WIDTH, 0)
            elif event.key == pygame.K_RIGHT:
                soldier_red_rect.move_ip(CELL_WIDTH, 0)
            elif event.key == pygame.K_UP:
                soldier_red_rect.move_ip(0, -CELL_HEIGHT)
            elif event.key == pygame.K_DOWN:
                soldier_red_rect.move_ip(0, CELL_HEIGHT)

    # Отрисовка игрового поля
    screen.fill(GREEN)
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            pygame.draw.rect(screen, BLACK, grid[i][j], 1)

    # Отрисовка фигуры солдатика
    pygame.draw.rect(screen, soldier_red_color, soldier_red_rect)
    pygame.draw.rect(screen, soldier_blue_color, soldier_blue_rect)

    # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()
