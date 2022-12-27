import pygame
import random
import math
import sys
import time
from time import sleep
from random import randint
 
# Initialize Pygame
pygame.init()

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255,255,102)

# Set the screen size
W = 800
H = 600

# Create the screen
dis = pygame.display.set_mode((W, H))

# Set the window caption
pygame.display.set_caption('Matko papa buchty')

# Initialize game state variables
game_over = False
game_close = False

# Initialize enemy position and list
enemy_pos = [random.randint(0,W-50),0]
enemy_list = [enemy_pos]

# Initialize score list
score_list = []

# Create a clock object
clock = pygame.time.Clock()

# Load and scale the buchta image
BUCHTA = pygame.image.load("mufin.png").convert()
BUCHTA = pygame.transform.scale(BUCHTA,(50,50))

# Load and scale the matko image
MATKO = pygame.image.load("matko.png").convert()
MATKO = pygame.transform.scale(MATKO,(50,50))

# Create a font object for the score text
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to draw the enemies
def enemy(enemy_list):
    for enemy_pos in enemy_list:
        # Load and scale the alien image
        alien = pygame.image.load("alien.jpg").convert()
        alien = pygame.transform.scale(alien, (50,50))
        # Draw the alien on the screen
        dis.blit(alien, (enemy_pos[0],enemy_pos[1]))

# Function to make the enemies fall
def enemy_fall(enemy_list):
    if enemy_pos[1] >= 0 and enemy_pos[1] < H:
        # Move the enemy down
        enemy_pos[1] += 5
    else:
        # Reset the enemy's position if it has reached the bottom of the screen
        enemy_pos[0] = random.randint(0,H-50)
        enemy_pos[1] = 0

# Function to draw the score on the screen
def Your_score(score):
    # Render the score text
    value = score_font.render("Zjedene buchty: " + str(score), True, red)
    # Draw the score text on the screen
    dis.blit(value, [0, 0])

# Initialize movement variables
m_l = False
m_r = False

# Function to detect collision between two objects
def detect_collision(x1,y1,bx1,by1):
    # Check if the two objects are overlapping in the x and y directions
    if (bx1 >= x1 and bx1 < (x1 +50)) or (x1 >= bx1 and x1 < (bx1+50)):
        if (by1 >= y1 and by1 < (y1 +50)) or (y1 >= by1 and y1 < (by1+50)):
            # Return True if the objects are colliding
            return True
    # Return False if the objects are not colliding
    return False

# Function to detect collision between matko and an enemy
def detect_collision_alien(x1,y1,enemy_pos):
    # Check if the matko and enemy are overlapping in the x and y directions
    if (enemy_pos[0] >= x1 and enemy_pos[0] < (x1 +50)) or (x1 >= enemy_pos[0] and x1 < (enemy_pos[0]+50)):
        if (enemy_pos[1] >= y1 and enemy_pos[1] < (y1 +50)) or (y1 >= enemy_pos[1] and y1 < (enemy_pos[1]+50)):
            # Return True if the matko and enemy are colliding
            return True
    # Return False if the matko and enemy are not colliding
    return False

# Display a message in the specified color on the game window
def message(msg, color):
    mesg = score_font.render(msg, True, red)
    dis.blit(mesg, [50, H / 3])

# Main game loop for the game
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
