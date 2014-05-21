im1='bird.png'
im2='back2.png'
im3='back1.jpg'
speed_front=200
cyan=(0,255,255)
green=(115,237,24)


import pygame,sys
import random
from pygame.locals import *

highname='rhythm das'
highscore=0
ax,x,y,set=1000,0,500,0
t=0
c=0
count=0


fread=open('high scores.txt','r')     #for high scores management

pygame.init()
screen=pygame.display.set_mode((1000,550),0,0)
background=pygame.image.load(im2).convert_alpha()
bird=pygame.image.load(im1).convert_alpha()
back=pygame.image.load(im3).convert()
screen.fill(cyan)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():

        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                c=1
    second=clock.tick()
    milli=second/1000.0
    df=milli*speed_front
    if c==1 and x<10:
        x+=1
        set=0
    else:
        x=0
        c=0

    y+=x
 
    y=y-set*set/1000
    set+=df
    #for acceleration
    screen.blit(back,(0,0))
    screen.blit(background,(0,0))
    screen.blit(bird,(200,550-y))

    #according to screen resolution polygon coordinates can be adjusted
    
    pygame.draw.polygon(screen,green,((ax,t-1000),(ax,t+150),(ax-40,t+150),(ax-40,t+180),(ax+100,t+180),(ax+100,t+150),(ax+60,t+150),(ax+60,t-1000)))
    pygame.draw.polygon(screen,green,((ax,550+t+1000),(ax,t+550-150),(ax-40,t+550-150),(ax-40,t+550-180),(ax+100,t+550-180),(ax+100,t+550-150),(ax+60,t+550-150),(ax+60,t+550+1000)))

    ax-=df

    #conditions for checking collision, here the resolution of my bird was 55*35. Resolution function can be used

    if y<0 or (ax-40<200 and ax + 100>200 and (550-y+35>t+550-180 or 550-y<t+ 180)):
        print 'game over\n Your Score:\t',count
        highname=fread.readlines()
        highscore=int(highname[1])
        pygame.quit()
        if(highscore<count):
            fwrite=open('e:/flappy/high scores.txt','w')
            highname[0]=raw_input('enter your name: ')+'\n'
            highname[1]=str(count)
            fwrite.writelines(highname)
        print '\n\nHIGHSCORE:\n%s%d'%(highname[0],int(highname[1]))
        
        sys.exit()
        #for random heights of the obstacles, here t is the height
    if ax<0:
        ax=1000
        count+=1
        t=160-(random.random()*1000)%320

    pygame.display.update()
    
