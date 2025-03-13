import pygame
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Snake') #nombre d eel window
clock = pygame.time.Clock()

background = pygame.image.load('SnakeBack.jpg') #origin is alawys top left (0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame.init()
            exit()

    screen.blit(background,(0,0)) #blit = draw me to that location
    #draw and update every element
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)



