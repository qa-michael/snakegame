import pygame
import random
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Snake') #nombre d eel window
clock = pygame.time.Clock()
test_score_font= pygame.font.Font(None, 50)

#background = pygame.image.load('img/SnakeBack.jpg').convert() #origin is alawys top left (0,0)
text_surface = test_score_font.render('Score',False,'black')

# player_surf = pygame.image.load('img/player.png')
# player_surf = pygame.transform.scale(player_surf,(50,50)) #adjusting player scle ro prevent premature colliding.
# player_rect= player_surf.get_rect(midleft=(100,300)) #rect allows for specific point of movement
# fruit_surf = pygame.image.load('img/red_square.png')
# fruit_surf = pygame.transform.scale(fruit_surf,(50,50))

#Define player and fruit
player = pygame.Rect(100,300,50,50)
fruit = pygame.Rect(random.randint(50, 650),random.randint(50,550),30,30) #random sapwn
pygame.draw.rect(screen,(255,0,0),player)
pygame.draw.rect(screen,(0,255,0),fruit)


#fruit spawning 
#def spawn_fruit():
#    x = random.randint(100,700) #within playable width
#    y = random.randint(100,600) # within playable height
#    return pygame.Rect(x,y,85, 85) #fruit rect #25 so it doesnt instantly collide

def spawn_fruit():
    return pygame.Rect(random.randint(50,650),random.randint(50,550),30,30)



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
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    #update movement
    if direction == "UP":
        player.y -= speed
    elif direction == "DOWN":
        player.y += speed
    elif direction == "LEFT":
        player.x -= speed
    elif direction == "RIGHT":
        player.x += speed


#New fruit for score
    if player.colliderect(fruit):
        fruit = spawn_fruit()
    #screen.blit(background,(0,0)) #blit = draw me to that location
    #screen.blit(text_surface,(300,15))

#default movement left 
    #player_rect.x += 1
    if player.right >= 865: 
        player.left = 100
        screen.fill((200,200,200)) #background gris
        pygame.draw.rect(screen, (0, 255, 0), player)
        pygame.draw.rect(screen, (255, 0, 0), fruit)
        screen.blit(text_surface,(300,15))
    #screen.blit(player) #The axis is now the previosly defined rect
    #screen.blit(fruit_score_surf,fruit_rect)

#fruit screen blit
        

    #draw and update every element 
    
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)
    #for smooth movement 



