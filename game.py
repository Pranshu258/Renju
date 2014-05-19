bif = "back.jpg"
mif = "mif.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(bif).convert()
mouse_c = pygame.image.load(mif).convert_alpha()

x, y = 0, 0
movex, movey = 0, 0
clock = pygame.time.Clock()
speed = 180

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -1
            elif event.key == K_RIGHT:
                movex = +1
            elif event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = +1
        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex = 0
            elif event.key == K_RIGHT:
                movex = 0
            elif event.key == K_UP:
                movey = 0
            elif event.key == K_DOWN:
                movey = 0
    milli = clock.tick()
    seconds = milli/1000.0
    dm = seconds*speed
    x+=movex
    y+=movey
    screen.blit(background, (0,0))
    screen.blit(mouse_c, (x, y))
    x = x+dm
    y = y+dm
    if x > 640:
        x = 0
    if y > 360:
        y = 0
    
    pygame.display.update()
