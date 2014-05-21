#importing images.
#background, moving image, aiming pointer, message images

bif = "back.jpg"
mif = "mif.png"
im='aim.png'
image='bam_logo.jpg'
display='oops.jpg'
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,300),0,32)

background = pygame.image.load(bif).convert()
mouse_c = pygame.image.load(mif).convert_alpha()
aim=pygame.image.load(im).convert_alpha()
bam=pygame.image.load(image).convert()
oops=pygame.image.load(display).convert()
x, y = 0, 0
ax,ay=0,0
c=0
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
        if event.type==MOUSEMOTION:
            ax=event.pos[0]
            ay=event.pos[1]
        if event.type==MOUSEBUTTONDOWN:
            c=1
        if event.type==MOUSEBUTTONUP:
            c=0
    second = clock.tick()
    milli = second/1000.0
    dm = milli*speed
    x+=movex
    y+=movey
    screen.blit(background, (0,0))
    screen.blit(mouse_c, (x, y))
    screen.blit(aim,(ax-25,ay-25))
    if c==1:
        if ax<x or ay<y or ax>x+333 or ay>y+312:        #checks if shot in target
            screen.blit(oops,(0,0))
        else:
            screen.blit(bam,(0,0))
    x = x+dm
    y = y+dm
    if x<0:
        x=0
    if y<0:
        y=0
    if x > 600:
        x = 0
    if y > 300:
        y =0
    
    pygame.display.update()

