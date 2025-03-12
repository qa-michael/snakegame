import pygame
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake') #nombre d eel window
clock = pygame.time.Clock()

test_surface = pygame.Surface((400,400)) #origin is alawys top left (0,0)
test_surface.fill('blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame.init()
            exit()

    screen.blit(test_surface,(0,0))
    #draw and update every element
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)



