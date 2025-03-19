import pygame
from character import character

player = character(x:0, y:0)
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

            