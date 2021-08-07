import pygame
import random
from pygame.constants import K_DOWN, K_RIGHT, K_UP
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Car runner")
icon = pygame.image.load("baby-car.png")
bg = pygame.image.load("download.png")
ucar = pygame.image.load("car (1).png")
enemyimg = []
enemyX = []
enemyY = []
enemychangeX = []
enemychangeY = []

k = 0
mixer.music.load("Blazer Rail 2.wav")
mixer.music.play(-1)
bg_images = []

for i in range(1,34):
    if(i<10):
        src = "bgimages\ezgif-frame-00" + str(i) +".jpg"
    else:
        src = "bgimages\ezgif-frame-0" + str(i) +".jpg"
    print(src)
    bg_images.append(pygame.image.load(src))


for i in range(0,3):
    enemyimg.append(pygame.image.load("car (3).png"))
    if(k==0):
        enemyX.append(330)
        enemyY.append(0)
        
        k=1
    elif(k == 1):
        enemyX.append(470)
        enemyY.append(0)
        
        k=2
    elif(k == 2):
        enemyX.append(400)
        enemyY.append(0)
    
    enemychangeY.append(1)


playerX = 370
playerY = 480
playerchangeX = 0
playerchangeY = 0

pygame.display.set_icon(icon)

def player(x,y):
    screen.blit(ucar,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def isCollision(x1,y1,x2,y2):
    
    if( 35 >= math.sqrt(((x2 - x1)**2) + ((y2-y1)**2))  >= -35):
        return True
    else:
        return False

    # playxl = x1 - 14
    # playyl = y1 - 23
    # playxr = x1 + 13
    # playyr = y1 - 23
    # start = playyl
    # end = playyl - 10

    # playarr = set()

    # for i in range(playxl,playxr +1.5,1.5):
    #     for j in range(start, end):
    #         if( j == end - 1 ):
    #             start = end -1
    #             end = start +1

    #         playarr.add(i,j)
    # i = playxl
    # j = start
    # while(i<x1+1.5):
    #     while(start < end):
    #         playarr.add((i,start))
    #         start+=1
    #     i+=1.5
    
    # i = x1+1
    # start = end - 1
    # end = playyl - 10

    # while(i<playxr+1.5):
    #     while(start < end):
    #         playarr.add((i,start))
    #         start-=1
    #     i+=1.5

    # compxl = x2 - 11
    # compyl = y2 + 28
    # compxr = x2 + 11
    # compyr = y2 + 28

    # comparr = set()

    # for i in range(compxl , compxr+1):
    #     for j in range(compyl , compyr+1):
    #         comparr.add((i,j))
    
    # if not(len(playarr.intersection(comparr)) == 0 ):
    #     return True
    # else:
    #     return False

scorev = 0
# font = pygame.font.Font('freesans.ttf',32)
font = pygame.font.SysFont("Segoe UI", 32)


def show_score():
    
    score = font.render("Score:" + str(scorev), True, (0,0,0))
    screen.blit(score,(10,10))

run = True
a = 1
b = 1

current_time = 0

j = 1

f = 0
speed = 60

score_changed = 10000

while run:
    
    if(j >= 32):
        j = 0
    
    if(j<0):
        j = 32

    screen.blit(bg_images[j],(0,0))
    print(speed)
   
    print(current_time)
    if(current_time > score_changed and speed > 2):
        
        speed -= 19
        score_changed += 10000
        for i in range(3):
            enemychangeY[i] += 0.3

    if(f % speed == 0):
        j += 1

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerchangeX -= 1
            if event.key == pygame.K_RIGHT:
                playerchangeX += 1
                
        if event.type == pygame.KEYUP:
            
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerchangeX = 0
                

    playerX += playerchangeX
    playerY += playerchangeY

    if(playerX < 270):
        playerX = 270

    if(playerX > 512):
        playerX = 512

    if(playerY<0):
        playerY = 0
    if(playerY > 540):
        playerY = 540

    for i in range(3):
        if(a and i ==1):
            continue
        if( b and i ==2):
            continue
        
        enemyY[i] += enemychangeY[i]

        if(enemyX[i] < 270):
            enemychangeX[i] = 1
           
        if(enemyX[i] > 512):
            enemychangeX[i] = -1
            
        if(enemyY[i] > 600):
            enemyY[i] = 0
            enemyX[i] = random.randint(270,512)

    if(enemyY[0] > 150 and a):
        enemy(enemyX[1],enemyY[1],1)
        a = 0 
    if(enemyY[0] > 350 and b):
        enemy(enemyX[2],enemyY[2],2)
        b = 0 

    for i in range(3):
        
        collision = isCollision(playerX,playerY,enemyX[i],enemyY[i])
        if collision:
            print("over")
            run = False

    enemy(enemyX[0],enemyY[0],0)
    if(a == 0):
        enemy(enemyX[1],enemyY[1],1)
    if(b == 0):
        enemy(enemyX[2],enemyY[2],2)

    player(playerX,playerY)
    
    current_time = pygame.time.get_ticks()
    scorev = current_time//1000

    show_score()

    f +=1
    pygame.display.update()