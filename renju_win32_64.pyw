import algo
import pygame, sys
from pygame.locals import *

#loading images
i_icon = "images\icon.png"
mode = "images\selectmode.jpg"
#third argument in mode1() is for differentiating between new and saved game
#1 means new game and 2 means saved game
#the game board
def mode1(u, enabled, s):
    undo = 1
    #reading the board theme
    fread = open('info\\theme.txt', 'r')
    default = "images\\"+fread.readline()
    fread.close()
    bif = default
    #if u = 0 then white otherwise black
    if u == 0:
        USER = "images\\blanc.png"
        AI = "images\\noir.png"
    elif u == 1:
        USER = "images\\noir.png"
        AI = "images\\blanc.png"
    #loading ingame images
    i_icon = "images\icon.png"
    EXIT = "images\exit.png"
    PANE = "images\pane.jpg"
    ABOUT = "images\\about.png"
    WIN = "images\win.png"
    LOSE = "images\lost.png"
    YOU = "images\you.png"
    ME = "images\me.png"
    UNDO = "images\disabled.png"
    AGAIN = "images\\again.png"
    NOTHING = "images\waste.png"    
    #initializing the arrays
    HUMAN = []
    COMPUTER = []
    pygame.init()
    #drawing the images on display surface
    icon = pygame.image.load(i_icon)
    pygame.display.set_icon(icon)
    #setting the screen to 960 x 640 resolution
    screen = pygame.display.set_mode((960,640),0,32)
    #loading the background and stone images
    background = pygame.image.load(bif).convert()
    pane = pygame.image.load(PANE).convert()
    about = pygame.image.load(ABOUT).convert_alpha()
    win  = pygame.image.load(WIN).convert_alpha()
    lost = pygame.image.load(LOSE).convert_alpha()
    no_undo = pygame.image.load(UNDO).convert_alpha()
    user = pygame.image.load(USER).convert_alpha()
    playAgain = pygame.image.load(AGAIN).convert_alpha()
    ai = pygame.image.load(AI).convert_alpha()
    you = pygame.image.load(YOU).convert_alpha()
    me = pygame.image.load(ME).convert_alpha()
    nothing = pygame.image.load(NOTHING).convert_alpha()
    escape = pygame.image.load(EXIT).convert_alpha()
    pygame.display.set_caption('RENJU')
    #loading the initial screen    
    screen.blit(background,(0,0))
    screen.blit(pane,(640,0))
    if not enabled:
        screen.blit(no_undo, (640, 25))
    #the first move (for new game)
    if s == 1:
        if u == 0:
            count = 1
            COMPUTER.append((300,300))
            screen.blit(ai ,(300,300))
            screen.blit(you, (650,400))
        elif u == 1:
            HUMAN.append((300,300))
            screen.blit(user ,(300,300))
            screen.blit(me, (650,400))
            count = 1
        pygame.display.update()
    #restoring the board if the game is a saved game
    elif s == 2:
        screen.blit(you, (650,400))
        fread = open('info\savedGame.txt', 'r')
        fread.readline()
        fread.readline()
        count = int(fread.readline())
        line = fread.readline()
        while not( line == "COMPUTER\n"):
            X = int(line)
            Y = int(fread.readline())
            HUMAN.append((X,Y))
            line = fread.readline()
        line = fread.readline()
        while not( line == "END\n"):
            X = int(line)
            Y = int(fread.readline())
            COMPUTER.append((X,Y))
            line = fread.readline()
        fread.close()
        i = 0
        while i < len(HUMAN):
            screen.blit(user, HUMAN[i] )
            pygame.display.update()
            i = i+1           
        i = 0
        while i < len(COMPUTER):
            screen.blit(ai, COMPUTER[i] )
            pygame.display.update()
            i = i+1
    #the game loop
    complete = False
    while True:         
        pos = [0,0]
        for event in pygame.event.get():
            #to quit when the user clicks the close button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #handling the display when it is minimized
            if event.type == ACTIVEEVENT or event.type == 17:
                i = 0
                while i < len(HUMAN):
                    screen.blit(user, HUMAN[i] )
                    pygame.display.update()
                    i = i+1           
                i = 0
                while i < len(COMPUTER):
                    screen.blit(ai, COMPUTER[i] )
                    pygame.display.update()
                    i = i+1                
            #we can detect the position where the player clicks
            if event.type == MOUSEBUTTONDOWN:                   
                pos  = list(event.pos)
                flag = 0
                if pos[0] > 640 and pos[0] < 960 and pos[1] > 0 and pos[1] < 23:
                    screen.blit(about,(640,87))                             
                    i = 0
                    while i < len(HUMAN):
                        screen.blit(user, HUMAN[i] )
                        pygame.display.update()
                        i = i+1           
                    i = 0
                    while i < len(COMPUTER):
                        screen.blit(ai, COMPUTER[i] )
                        pygame.display.update()
                        i = i+1
                #restart game
                if pos[0] > 670 and pos[0] < 760 and pos[1] > 500 and pos[1] < 590:
                    del(HUMAN)
                    del(COMPUTER)                   
                    mode1(u, enabled, 1)
                #quit to main menu
                if pos[0] > 790 and pos[0] < 940 and pos[1] > 400 and pos[1] < 476:
                    del(HUMAN)
                    del(COMPUTER)
                    pygame.quit()
                    select()
                #save unfinished game
                if pos[0] > 790 and pos[0] < 940 and pos[1] > 500 and pos[1] < 590:
                    if not complete:
                        fwrite = open('info\savedGame.txt', 'w')
                        fwrite.write(str(u)+"\n")
                        fwrite.write(str(enabled)+"\n")
                        fwrite.write(str(count)+"\n")
                        i = 0
                        while i < len(HUMAN):
                            a = list(HUMAN[i])
                            fwrite.writelines(str(a[0])+"\n"+str(a[1])+"\n")
                            i = i+1           
                        i = 0
                        fwrite.write("COMPUTER\n")
                        while i < len(COMPUTER):
                            a = list(COMPUTER[i])
                            fwrite.writelines(str(a[0])+"\n"+str(a[1])+"\n")
                            i = i+1
                        fwrite.write("END\n")
                        fwrite.close()
                        pygame.quit()
                        sys.exit()
                    #if game is complete exit without saving
                    elif complete:
                        pygame.quit()
                        sys.exit()
                if (count%2 == 1 and u == 0) or (count%2 == 0 and u == 1) :
                    #undo move
                    if pos[0] > 640 and pos[0] < 960 and pos[1] > 25 and pos[1] < 90 and count > 2:
                        #if undo move is available and enabled then
                        if undo == 1 and not complete and enabled:
                            undo = 0
                            del(HUMAN[len(HUMAN)-1])
                            del(COMPUTER[len(COMPUTER)-1])
                            count = count-2
                            i = 0
                            while i < len(HUMAN):
                                screen.blit(user, HUMAN[i] )
                                pygame.display.update()
                                i = i+1           
                            i = 0
                            while i < len(COMPUTER):
                                screen.blit(ai, COMPUTER[i] )
                                pygame.display.update()
                                i = i+1
                    
                    #make move
                    if pos[0] > 20 and pos[0] < 620 and pos[1] > 20 and pos[1] < 620 and not complete:
                        flag = 1
                    #finding the position at which the stones are to be placed
                    if flag == 1:
                        
                        X = pos[0]- pos[0]%40
                        if pos[0]%40 > 40-pos[0]%40:
                            X = X+40
                        X = X-20
                        Y = pos[1]- pos[1]%40
                        if pos[1]%40 > 40-pos[1]%40:
                            Y = Y+40
                        Y = Y-20
                        #checking if the move is valid    
                        j = 0
                        while j < len(HUMAN):
                            if X == HUMAN[j][0] and Y == HUMAN[j][1]:
                                flag = 0
                                break
                            j = j+1
                        j = 0
                        while j < len(COMPUTER):
                            if X == COMPUTER[j][0] and Y == COMPUTER[j][1]:
                                flag = 0
                                break
                            j = j+1
                    #appending the coin to the human player
                    if flag == 1:
                        undo = 1
                        screen.blit(me, (650,400))
                        HUMAN.append((X,Y))
                        i = 0
                        while i < len(HUMAN):
                            screen.blit(user, HUMAN[i] )
                            pygame.display.update()
                            i = i+1           
                        i = 0
                        while i < len(COMPUTER):
                            screen.blit(ai, COMPUTER[i] )
                            pygame.display.update()
                            i = i+1          
                        temp = 0
                        #checking after each step if the player has done five in a line
                        #SEARCHING FOR FIVES
                        #HORIZONTAL 
                        if (X+40,Y) in HUMAN and (X+80,Y) in HUMAN and (X+120,Y) in HUMAN and (X+160,Y) in HUMAN:
                            temp = 1
                        elif (X-40,Y) in HUMAN and (X-80,Y) in HUMAN and (X-120,Y) in HUMAN and (X-160,Y) in HUMAN:
                            temp = 1
                        #VERTICAL 
                        elif (X,Y+40) in HUMAN and (X,Y+80) in HUMAN and (X,Y+120) in HUMAN and (X,Y+160) in HUMAN:
                            temp = 1
                        elif (X,Y-40) in HUMAN and (X,Y-80) in HUMAN and (X,Y-120) in HUMAN and (X,Y-160) in HUMAN:
                            temp = 1
                        #SOUTHEAST 
                        elif (X+40,Y+40) in HUMAN and (X+80,Y+80) in HUMAN and (X+120,Y+120) in HUMAN and (X+160,Y+160) in HUMAN:
                            temp = 1
                        elif (X-40,Y-40) in HUMAN and (X-80,Y-80) in HUMAN and (X-120,Y-120) in HUMAN and (X-160,Y-160) in HUMAN:
                            temp = 1
                        #SOUTHWEST 
                        elif (X-40,Y+40) in HUMAN and (X-80,Y+80) in HUMAN and (X-120,Y+120) in HUMAN and (X-160,Y+160) in HUMAN:
                            temp = 1
                        elif (X+40,Y-40) in HUMAN and (X+80,Y-80) in HUMAN and (X+120,Y-120) in HUMAN and (X+160,Y-160) in HUMAN:
                            temp = 1
                        #HORIZONTAL
                        elif (X-40,Y) in HUMAN and (X+40,Y) in HUMAN and (X+80,Y) in HUMAN and (X+120,Y) in HUMAN:
                            temp = 1
                        elif (X-80,Y) in HUMAN and (X-40,Y) in HUMAN and (X+40,Y) in HUMAN and (X+80,Y) in HUMAN:
                            temp = 1
                        elif (X-120,Y) in HUMAN and (X-80,Y) in HUMAN and (X-40,Y) in HUMAN and (X+40,Y) in HUMAN:
                            temp = 1
                        #SOUTHEAST
                        elif (X-40,Y-40) in HUMAN and (X+40,Y+40) in HUMAN and (X+80,Y+80) in HUMAN and (X+120,Y+120) in HUMAN:
                            temp = 1
                        elif (X-80,Y-80) in HUMAN and (X-40,Y-40) in HUMAN and (X+40,Y+40) in HUMAN and (X+80,Y+80) in HUMAN:
                            temp = 1
                        elif (X-120,Y-120) in HUMAN and (X-80,Y-80) in HUMAN and (X-40,Y-40) in HUMAN and (X+40,Y+40) in HUMAN:
                            temp = 1
                        #SOUTHWEST
                        elif (X-40,Y+40) in HUMAN and (X+40,Y-40) in HUMAN and (X+80,Y-80) in HUMAN and (X+120,Y-120) in HUMAN:
                            temp = 1
                        elif (X-80,Y+80) in HUMAN and (X-40,Y+40) in HUMAN and (X+40,Y-40) in HUMAN and (X+80,Y-80) in HUMAN:
                            temp = 1
                        elif (X-120,Y+120) in HUMAN and (X-80,Y+80) in HUMAN and (X-40,Y+40) in HUMAN and (X+40,Y-40) in HUMAN:
                            temp = 1
                        #VERTICAL
                        elif (X,Y-40) in HUMAN and (X,Y+40) in HUMAN and (X,Y+80) in HUMAN and (X,Y+120) in HUMAN:
                            temp = 1
                        elif (X,Y-80) in HUMAN and (X,Y-40) in HUMAN and (X,Y+40) in HUMAN and (X,Y+80) in HUMAN:
                            temp = 1
                        elif (X,Y-120) in HUMAN and (X,Y-80) in HUMAN and (X,Y-40) in HUMAN and (X,Y+40) in HUMAN:
                            temp = 1

                        #declaring the winner
                        if temp == 1:
                            screen.blit(nothing, (650,400))
                            screen.blit(win,(640,87))
                            screen.blit(escape, (790,500))
                            screen.blit(playAgain, (670, 500))
                            i = 0
                            while i < len(HUMAN):
                                screen.blit(user, HUMAN[i] )
                                pygame.display.update()
                                i = i+1           
                            i = 0
                            while i < len(COMPUTER):
                                screen.blit(ai, COMPUTER[i] )
                                pygame.display.update()
                                i = i+1                      
                            pygame.display.update()
                            complete = True
                        count = count+1
            #the computer player       
            if ((count%2 == 0 and u == 0) or (count%2 == 1 and u == 1)) and not complete:
		#the ai command
                algo.attack(COMPUTER, HUMAN, 0, 6, -1000, 1000)
                screen.blit(you, (650,400))
                pygame.display.update()
                i = 0
                while i < len(HUMAN):
                    screen.blit(user, HUMAN[i] )
                    pygame.display.update()
                    i = i+1           
                i = 0
                while i < len(COMPUTER):
                    screen.blit(ai, COMPUTER[i] )
                    pygame.display.update()
                    i = i+1                
                X = COMPUTER[len(COMPUTER)-1][0]
                Y = COMPUTER[len(COMPUTER)-1][1]
                #checking after each step if any of the player has done five in a line
                temp = 0
                #SEARCHING FOR FIVES
                #HORIZONTAL 
                if (X+40,Y) in COMPUTER and (X+80,Y) in COMPUTER and (X+120,Y) in COMPUTER and (X+160,Y) in COMPUTER:
                    temp = 1
                elif (X-40,Y) in COMPUTER and (X-80,Y) in COMPUTER and (X-120,Y) in COMPUTER and (X-160,Y) in COMPUTER:
                    temp = 1
                #VERTICAL 
                elif (X,Y+40) in COMPUTER and (X,Y+80) in COMPUTER and (X,Y+120) in COMPUTER and (X,Y+160) in COMPUTER:
                    temp = 1
                elif (X,Y-40) in COMPUTER and (X,Y-80) in COMPUTER and (X,Y-120) in COMPUTER and (X,Y-160) in COMPUTER:
                    temp = 1
                #SOUTHEAST 
                elif (X+40,Y+40) in COMPUTER and (X+80,Y+80) in COMPUTER and (X+120,Y+120) in COMPUTER and (X+160,Y+160) in COMPUTER:
                    temp = 1
                elif (X-40,Y-40) in COMPUTER and (X-80,Y-80) in COMPUTER and (X-120,Y-120) in COMPUTER and (X-160,Y-160) in COMPUTER:
                    temp = 1
                #SOUTHWEST 
                elif (X-40,Y+40) in COMPUTER and (X-80,Y+80) in COMPUTER and (X-120,Y+120) in COMPUTER and (X-160,Y+160) in COMPUTER:
                    temp = 1
                elif (X+40,Y-40) in COMPUTER and (X+80,Y-80) in COMPUTER and (X+120,Y-120) in COMPUTER and (X+160,Y-160) in COMPUTER:
                    temp = 1
                #HORIZONTAL
                elif (X-40,Y) in COMPUTER and (X+40,Y) in COMPUTER and (X+80,Y) in COMPUTER and (X+120,Y) in COMPUTER:
                    temp = 1
                elif (X-80,Y) in COMPUTER and (X-40,Y) in COMPUTER and (X+40,Y) in COMPUTER and (X+80,Y) in COMPUTER:
                    temp = 1
                elif (X-120,Y) in COMPUTER and (X-80,Y) in COMPUTER and (X-40,Y) in COMPUTER and (X+40,Y) in COMPUTER:
                    temp = 1
                #SOUTHEAST
                elif (X-40,Y-40) in COMPUTER and (X+40,Y+40) in COMPUTER and (X+80,Y+80) in COMPUTER and (X+120,Y+120) in COMPUTER:
                    temp = 1
                elif (X-80,Y-80) in COMPUTER and (X-40,Y-40) in COMPUTER and (X+40,Y+40) in COMPUTER and (X+80,Y+80) in COMPUTER:
                    temp = 1
                elif (X-120,Y-120) in COMPUTER and (X-80,Y-80) in COMPUTER and (X-40,Y-40) in COMPUTER and (X+40,Y+40) in COMPUTER:
                    temp = 1
                #SOUTHWEST
                elif (X-40,Y+40) in COMPUTER and (X+40,Y-40) in COMPUTER and (X+80,Y-80) in COMPUTER and (X+120,Y-120) in COMPUTER:
                    temp = 1
                elif (X-80,Y+80) in COMPUTER and (X-40,Y+40) in COMPUTER and (X+40,Y-40) in COMPUTER and (X+80,Y-80) in COMPUTER:
                    temp = 1
                elif (X-120,Y+120) in COMPUTER and (X-80,Y+80) in COMPUTER and (X-40,Y+40) in COMPUTER and (X+40,Y-40) in COMPUTER:
                    temp = 1
                #VERTICAL
                elif (X,Y-40) in COMPUTER and (X,Y+40) in COMPUTER and (X,Y+80) in COMPUTER and (X,Y+120) in COMPUTER:
                    temp = 1
                elif (X,Y-80) in COMPUTER and (X,Y-40) in COMPUTER and (X,Y+40) in COMPUTER and (X,Y+80) in COMPUTER:
                    temp = 1
                elif (X,Y-120) in COMPUTER and (X,Y-80) in COMPUTER and (X,Y-40) in COMPUTER and (X,Y+40) in COMPUTER:
                    temp = 1

                #declaring the winner
                if temp == 1:
                    screen.blit(nothing , (650,400))
                    screen.blit(lost,(640,87))
                    screen.blit(escape, (790,500))
                    screen.blit(playAgain, (670, 500))
                    i = 0
                    while i < len(HUMAN):
                        screen.blit(user, HUMAN[i] )
                        pygame.display.update()
                        i = i+1           
                    i = 0
                    while i < len(COMPUTER):
                        screen.blit(ai, COMPUTER[i] )
                        pygame.display.update()
                        i = i+1                      
                    pygame.display.update()
                    complete = True
                count = count +1         
        screen.blit(background,(0,0))

#color select window     
def select():
    user = 0
    undo = 0
    pygame.init()
    OPTIONS = "images\select.png"
    WINDOW1 = pygame.display.set_mode((660, 390))
    pygame.display.set_caption("RENJU")
    icon = pygame.image.load(i_icon)
    options = pygame.image.load(OPTIONS).convert_alpha()
    WINDOW1.blit(options,(0,0))
    pygame.display.set_icon(icon)
    while True:
        pos = [0, 0]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = list(event.pos)
                if pos[1] < 318 and pos[1] > 0:
                    if pos[0] < 330 and pos[0] > 0:
                        user = 1
                    if pos[0] < 660 and pos[0] > 330:
                        user = 0
                if pos[1] < 360 and pos[1] > 318: 
                    if pos[0] < 660 and pos[0] > 440:
                        pygame.quit()
                        mode1(user, undo, 1)
                    if pos[0] < 440 and pos[0] > 220:
                            undo = 1
                    if pos[0] < 220 and pos[0] > 0:
                            fread = open('info\\theme.txt', 'r')
                            prev = fread.readline()
                            fread.close()
                            img = list(prev)
                            img[4] = str((int(img[4])+1)%7)
                            fwrite = open('info\\theme.txt', 'w')
                            i = 0
                            while i < len(img):
                                fwrite.writelines(img[i])
                                i = i+1
                            fwrite.close()
        pygame.display.update()

#initializing the game loop
pygame.init()
WINDOW1 = pygame.display.set_mode((660, 390))
pygame.display.set_caption("RENJU")
icon = pygame.image.load(i_icon)
background = pygame.image.load(mode).convert()
WINDOW1.blit(background,(0,0))
pygame.display.set_icon(icon)
while True:
    pos = [0, 0]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = list(event.pos)
            #new game
            if pos[1] < 370 and pos[1] > 20:
                if pos[0] < 320 and pos[0] > 20:
                    select()
            #resume last saved game
            if pos[0] > 340 and pos[0] < 660 and pos[1] > 0 and pos[1] < 100:
                fread = open('info\savedGame.txt', 'r')
                u = int(fread.readline())
                e = int(fread.readline())
                fread.close()
                mode1(u, e, 2)
    pygame.display.update()

