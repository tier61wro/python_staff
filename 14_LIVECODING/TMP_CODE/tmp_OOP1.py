import pygame
import random

WIDTH = 900
HEIGHT = 800
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPACE_COLOUR = (25, 20, 50)

pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY game")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    screen.fill(SPACE_COLOUR)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            print("Mouse was moved")


        if event.type == pygame.KEYDOWN:
            # print("KEYDOWN")
            if event.key == pygame.K_LEFT:
                print("K_LEFT")

pygame.quit