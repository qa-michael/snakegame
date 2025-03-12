import pygame
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake') #nombre d eel window

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame.init()
            exit()
    #draw and update every element
    pygame.display.update()
