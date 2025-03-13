import pygame
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Snake') #nombre d eel window
clock = pygame.time.Clock()
test_score_font= pygame.font.Font(None, 50)

background = pygame.image.load('img/SnakeBack.jpg').convert() #origin is alawys top left (0,0)
text_surface = test_score_font.render('Score',False,'Red')

player_surf = pygame.image.load('img/Player_Square.webp')
player_rect= player_surf.get_rect(midleft=(100,300)) #rect allows for specific point of movement

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame.init()
            exit()

    screen.blit(background,(0,0)) #blit = draw me to that location
    screen.blit(text_surface,(300,15))
    screen.blit(player_surf,player_rect) #The axis is now the previosly defined rect
    #draw and update every element
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)



