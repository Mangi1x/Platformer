import pygame as pg 
import random
from time import sleep
pg.init()

SCREEN_WIDTH = 500

SCREEN_HEIGHT = 500

win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

bg = pg.image.load('bg.png')

player_hitbox_x = 45

player_hitbox_y = 71

player2_hitbox_q = 60

player2_hitbox_e = 53

player_first = [ pg.image.load('player.png'),
              pg.image.load('pl2.png'),
              pg.image.load('anim.png'),
              pg.image.load('moreanim.png')
]
player_second = pg.image.load('playertwo.png')

player_second2 = pg.image.load('playertwo2.png')

ceiling = SCREEN_HEIGHT - player_hitbox_y

ceiling2 = SCREEN_HEIGHT - player2_hitbox_e

wall = SCREEN_WIDTH - player_hitbox_x

wall2 = SCREEN_WIDTH - player2_hitbox_q

x = 0

y = 429

q = 50

e = 15

l = 100

z = -150

find_player = player_hitbox_x - x

anim_count = 0

anim_count2 = 0

speed = 0.5

speed2 = 0.5

speed3 = 0.5

run = True

clock = pg.time.Clock() 

trans_collor = pg.Color(255, 255, 255)

player_second.set_colorkey(trans_collor)

player_second2.set_colorkey(trans_collor)

point = 0

q = random.randint(1,455)

l = random.randint(1,455)

while(run):
    pg.display.set_caption("Platformer")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
    
    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        x-=speed
        if anim_count == 2:
            anim_count = 0
        else:
            anim_count += 1
    if keys[pg.K_d]:
        x+=speed
        if anim_count == 2:
            anim_count = 0
        else:
            anim_count += 1
    if keys[pg.K_ESCAPE]:
        run = False
        print("You leave the game!")

    if e >= 410:
        if (x) == (q):
                e = 0
                q = random.randint(0, 455)
                point += 1
                print(point)
    if z >= 410:
        if (x) == (l):
                z = 0
                l = random.randint(0, 455)
                point += 1
                
                print(point)
    

    z += speed

    if e == 444:
        point -= 1
        print(point)
        e = 0
    
    if z == 444:
        point -= 1
        print(point)
        z = 0
    
    for i in range(run):
        e += speed2

    if x <= 0:
        x = 1
    
    if x >= wall:
        
        x = wall
    
    if y <= 0:
        y = 1
    
    if y >= ceiling:
        
        y = ceiling

    if q <= 0:
        q = 1
    
    if q >= wall2:
        
        q = wall2
    
    if e <= 0:
        e = 1
    
    if e >= ceiling2:
        
        e = ceiling2

    if point < -3:
        print("You lose :(")
        run = False


    if point == 10:
        print("You win!")
        run = False

    win.blit(player_first[anim_count],(x,y))

    pg.display.update()

    win.blit(player_second, (q,e))

    pg.display.update()

    win.blit(player_second2,(l,z))

    pg.display.update()

    win.fill((0,0,0))

    win.blit(bg,(0,0))

    clock.tick(0)
pg.quit()