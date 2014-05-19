#We have used the pygame library to make a game something like the flappy bird
#bif is the background image file
#mif is the moving image file
bif = "back.jpg"
mif = "mif.png"
#importing the libraries
import pygame, sys
from pygame.locals import *

pygame.init()
#setting the screen to 640 x 360 resolutin
screen = pygame.display.set_mode((640,360),0,32)
#loading the background and moving images
background = pygame.image.load(bif).convert()
mouse_c = pygame.image.load(mif).convert_alpha()
#initial position of the moving image
x, y = 1, 1
movex, movey = 0, 0
#to measure time (we will use this to decrease the speed of the moving image)
#because by default its speed is high
clock = pygame.time.Clock()
speed = 200
#counting score
score = 0
#the game loop
while True:
    
    for event in pygame.event.get():
        #to quit when the user clicks the close button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #these statements let the player to move the figure in desired direction using the arrow keys
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -1
            elif event.key == K_RIGHT:
                movex = +1
            elif event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = +1
        #these statements leave the figure on its own again as soon as the player leaves the key 
        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex = 0
            elif event.key == K_RIGHT:
                movex = 0
            elif event.key == K_UP:
                movey = 0
            elif event.key == K_DOWN:
                movey = 0
    #the following three lines decrease the moving speed of the figure
    milli = clock.tick()
    seconds = milli/1000.0
    dm = seconds*speed
    #to change the co-ordinates of the moving figure according to the arrow keys pressed by the user
    #note that the co-ordinates refer to the upper left corner of the moving figure
    x+=movex
    y+=movey
    #these statements display the figures according to the changing co-ordinates
    screen.blit(background, (0,0))
    screen.blit(mouse_c, (x, y))
    #the automatic movement of the figure
    x = x+dm
    y = y+dm
    #counting score when the figure ends up at right edge of window and emerges from the left
    if x > 640:
        x = 0
        score = score + 100
    #if the moving figure touches the upper or lower edges of the window the game ends  
    if y <= 0 or y > 254:
        print 'GAME OVER  \nYou scored : '
        print score
        pygame.quit()
        sys.exit()
        
    pygame.display.update()
