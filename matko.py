import pygame
import random
import math
import sys
import time
from time import sleep
from random import randint
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255,255,102)
W = 800
H = 600
 
dis = pygame.display.set_mode((W, H))
pygame.display.set_caption('Matko papa buchty')
 
game_over = False
game_close = False

enemy_pos = [random.randint(0,W-50),0]
enemy_list = [enemy_pos]
 
score_list = []

clock = pygame.time.Clock()

BUCHTA = pygame.image.load("mufin.png").convert()
BUCHTA = pygame.transform.scale(BUCHTA,(50,50))

MATKO = pygame.image.load("matko.png").convert()
MATKO = pygame.transform.scale(MATKO,(50,50))
score_font = pygame.font.SysFont("comicsansms", 35)

def enemy(enemy_list):
    for enemy_pos in enemy_list:
        alien = pygame.image.load("alien.jpg").convert()
        alien = pygame.transform.scale(alien, (50,50))
        dis.blit(alien, (enemy_pos[0],enemy_pos[1]))
def enemy_fall(enemy_list):
    if enemy_pos[1] >= 0 and enemy_pos[1] < H:
        enemy_pos[1] += 5
    else:
        enemy_pos[0] = random.randint(0,H-50)
        enemy_pos[1] = 0

def Your_score(score):
    value = score_font.render("Zjedene buchty: " + str(score), True, red)
    dis.blit(value, [0, 0])

m_l = False
m_r = False

def detect_collision(x1,y1,bx1,by1):
    if (bx1 >= x1 and bx1 < (x1 +50)) or (x1 >= bx1 and x1 < (bx1+50)):
        if (by1 >= y1 and by1 < (y1 +50)) or (y1 >= by1 and y1 < (by1+50)):
            return True
    return False
def detect_collision_alien(x1,y1,enemy_pos):
    if (enemy_pos[0] >= x1 and enemy_pos[0] < (x1 +50)) or (x1 >= enemy_pos[0] and x1 < (enemy_pos[0]+50)):
        if (enemy_pos[1] >= y1 and enemy_pos[1] < (y1 +50)) or (y1 >= enemy_pos[1] and y1 < (enemy_pos[1]+50)):
            return True
    return False
 
def message(msg, color):
    mesg = score_font.render(msg, True, red)
    dis.blit(mesg, [50, H / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = 300
    y1 = 550
    m_l = False
    m_r = False
    by1 = 0
    bx1 = 100
    score = 0
    score_list = []

    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("Zjedol ta mimozemstan. Stlač C pre hru alebo Q pre koniec", black)
            Your_score(score)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    m_r = True
                if event.key == pygame.K_LEFT:
                    m_l = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    m_r = False
                if event.key == pygame.K_LEFT:
                    m_l = False

        if x1 >= 750:
            x1 = 750
        elif x1 < 0:
            x1 = 0

        if m_r:
            x1 += 5
        if m_l:
            x1 -= 5
                
        if by1 >= 0 and by1 < H:
            by1 += 5
        else:
            bx1 = random.randint(0,H-50)
            by1 = 0
        
        if detect_collision(x1,y1,bx1,by1):
            bx1 = random.randint (0,H-50)
            by1 = 0
            score = score + 1
        if detect_collision_alien(x1,y1,enemy_pos):
            game_close = True



        dis.fill(black)
        enemy_fall(enemy_list)
        Your_score(score)
        enemy(enemy_list)
        dis.blit(MATKO,(x1,y1))

        dis.blit(BUCHTA, (bx1,by1))
  
        pygame.display.update()
    
        clock.tick(60)

    pygame.quit()
    quit()

gameLoop()