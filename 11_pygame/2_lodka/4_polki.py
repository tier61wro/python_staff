import pygame

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 1200
screen_height = 800

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игровое поле")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Размеры ячеек игрового поля
cell_width = 50
cell_height = 50

# Создание сетки из квадратов
for row in range(0, screen_height, cell_height):
    for column in range(0, screen_width, cell_width):
        pygame.draw.rect(screen, white, [column, row, cell_width, cell_height], 1)

# Создание красного солдатика
red_soldier_image = pygame.Surface((cell_width, cell_height))
red_soldier_image.fill(red)

# Создание синего солдатика
blue_soldier_image = pygame.Surface((cell_width, cell_height))
blue_soldier_image.fill(blue)

# Начальные координаты красного солдатика
red_soldier_x = 100
red_soldier_y = 100

# Начальные координаты синего солдатика
blue_soldier_x = 300
blue_soldier_y = 100

# Отрисовка солдатиков на игровом поле
screen.blit(red_soldier_image, (red_soldier_x, red_soldier_y))
screen.blit(blue_soldier_image, (blue_soldier_x, blue_soldier_y))

# Обновление экрана
pygame.display.flip()

# Запуск игрового цикла
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Перемещение красного солдатика с помощью стрелок на клавиатуре
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                red_soldier_x -= cell_width
            elif event.key == pygame.K_RIGHT:
                red_soldier_x += cell_width
            elif event.key == pygame.K_UP:
                red_soldier_y -= cell_height
            elif event.key == pygame.K_DOWN:
                red_soldier_y += cell_height

        # # Перемещение синего солдатика с помощью мыши
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if blue_soldier_image.get_rect().collidepoint(event.pos):
        #         selected_soldier = blue_soldier_image
        #     elif red_soldier_image.get_rect().collidepoint(event.pos):
        #         selected_soldier = red_soldier_image
