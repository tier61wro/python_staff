import pygame
import time
file = './music/1_torpeda.wav'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
time.sleep(10)
