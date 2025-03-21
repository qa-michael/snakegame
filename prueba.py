import pygame
import random
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Snake') #nombre del window
clock = pygame.time.Clock()

score = 0
font= pygame.font.Font(None, 50)

#Define player and fruit
#player = pygame.Rect(100,300,50,50)
snake_body = [pygame.Rect(100,300,50,50)] #snake is now a list
fruit = pygame.Rect(random.randint(50, 650),random.randint(50,550),30,30) #random sapwn
#pygame.draw.rect(screen,(255,0,0),player)
pygame.draw.rect(screen,(0,255,0),fruit)

def spawn_fruit():
    return pygame.Rect(random.randint(50,650),random.randint(50,550),30,30)

#Movement variables 

direction = "NULL"
speed = 4.5 

#GAME LOOP
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
    new_head = snake_body[0].copy()
    if direction == "UP":
        new_head.y -= speed
    elif direction == "DOWN":
        new_head.y += speed
    elif direction == "LEFT":
        new_head.x -= speed
    elif direction == "RIGHT":
        new_head.x += speed

#New fruit for score
    if new_head.colliderect(fruit):
        fruit = spawn_fruit()
        score += 1 
    else:
        snake_body.pop()

    snake_body.insert(0, new_head) #si se come fruta se inserta new snakebody

    if new_head.right >= 700: new_head.left = 100
    if new_head.left <= 0: new_head.right = 100
    if new_head.bottom <= 45: new_head.top = 100
    if new_head.top >= 550: new_head.bottom = 100
    screen.fill((200,200,200)) #background gris
    #pygame.draw.rect(screen, (0, 255, 0), new_head)
    pygame.draw.rect(screen, (255, 0, 0), fruit)

    for segment in snake_body:
        pygame.draw.rect(screen,(0,255,0),segment)

    score_surface = font.render(f"score: {score}", True, (0,0,0))
    screen.blit(score_surface, (300,20))
  
    #draw and update every element 
    
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)
    #for smooth movement 