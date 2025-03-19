import pygame
import random
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Snake') #nombre d eel window
clock = pygame.time.Clock()
test_score_font= pygame.font.Font(None, 50)

background = pygame.image.load('img/SnakeBack.jpg').convert() #origin is alawys top left (0,0)
text_surface = test_score_font.render('Score',False,'Red')

player_surf = pygame.image.load('img/player.png')
player_surf = pygame.transform.scale(player_surf,(50,50)) #adjusting player scle ro prevent premature colliding.
player_rect= player_surf.get_rect(midleft=(100,300)) #rect allows for specific point of movement
fruit_surf = pygame.image.load('img/red_square.png')
fruit_surf = pygame.transform.scale(fruit_surf,(50,50))


#fruit spawning 
def spawn_fruit():
    x = random.randint(100,700 - fruit_surf.get_width()) #within playable width
    y = random.randint(100,600 - fruit_surf.get_height()) # within playable height
    return pygame.Rect(x,y,85, 85) #fruit rect #25 so it doesnt instantly collide

fruit_rect = spawn_fruit()

#Movement variables 

direction = "RIGHT"
speed = 4 
#fruit_score_surf = pygame.image.load('img/3_hearts.png')
#fruit_rect = fruit_score_surf.get_rect(midleft = (600,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame.init()
            exit()
        
        #key press check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN:":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    #update movement
    if direction == "UP":
        player_rect.y -= speed
    elif direction == "DOWN":
        player_rect.y += speed
    elif direction == "LEFT":
        player_rect.x -= speed
    elif direction == "RIGHT":
        player_rect.x += speed


#New fruit for score
    if player_rect.colliderect(fruit_rect):
        fruit_rect = spawn_fruit()
    

    screen.blit(background,(0,0)) #blit = draw me to that location
    screen.blit(text_surface,(300,15))

#default movement left 
    #player_rect.x += 1
    if player_rect.right >= 865: player_rect.left = 100
    
    screen.blit(player_surf,player_rect) #The axis is now the previosly defined rect
    #screen.blit(fruit_score_surf,fruit_rect)

#fruit screen blit
    screen.blit(fruit_surf, fruit_rect)

    #draw and update every element 
    
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)
    #for smooth movement 



