import pygame
import random
from sys import exit #usando funcion specifica (from en vez de import)

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Snake') #nombre d eel window
clock = pygame.time.Clock()

score = 0
font= pygame.font.Font(None, 50)

#text_surface = test_score_font.render('Score',False,'black')

#Define player and fruit
player = pygame.Rect(100,300,50,50)
fruit = pygame.Rect(random.randint(50, 650),random.randint(50,550),30,30) #random sapwn
pygame.draw.rect(screen,(255,0,0),player)
pygame.draw.rect(screen,(0,255,0),fruit)

def spawn_fruit():
    return pygame.Rect(random.randint(50,650),random.randint(50,550),30,30)

#Movement variables 

direction = ""
speed = 4.5 

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
        score += 1 

    if player.right >= 700:player.left = 100
    if player.left <= 0: player.right = 100
    if player.bottom <= 45: player.top = 100
    if player.top >= 550: player.bottom = 100
    screen.fill((200,200,200)) #background gris
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), fruit)
    #screen.blit(text_surface,(300,15))

    score_surface = font.render(f"score: {score}", True, (0,0,0))
    screen.blit(score_surface, (300,20))

        
    #draw and update every element 
    
    pygame.display.update()
    clock.tick(60) #60 times per second (max framerate)
    #for smooth movement 