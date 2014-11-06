import wx
import algo
import pygame, sys
from pygame.locals import *

class renju(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id, 'RENJU', size = (1306,768))
        panel = wx.Panel(self)
        #the one player button
        pic4 = wx.Image("oneplayer.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic4, pos = (30, 140))
        self.Bind(wx.EVT_BUTTON, self.regist, self.button)
        self.button.SetDefault()
        #the new game two player button
        pic = wx.Image("twoplayer.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic, pos = (335, 140))
        self.Bind(wx.EVT_BUTTON, self.dome, self.button)
        self.button.SetDefault()    
        #the about renju button
        pic3 = wx.Image("about.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic3, pos = (945, 140))
        self.Bind(wx.EVT_BUTTON, self.about, self.button)
        #the themes button
        pic5 = wx.Image("themes.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic5, pos = (640, 140))
        self.Bind(wx.EVT_BUTTON, self.theme, self.button)
        #static text
        text = wx.StaticText(panel, -1, "RENJU - FIVE IN A LINE", (30, 10))
        font = wx.Font(80, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        text.SetForegroundColour((0,0,128))
        text.SetFont(font)
        text = wx.StaticText(panel, -1, "RENJU", (10, 500))
        font = wx.Font(240, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        text.SetForegroundColour((225,225,225))
        text.SetFont(font)
        text = wx.StaticText(panel, -1, "FIVE IN A LINE", (32, 510))
        font = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        text.SetForegroundColour((225,225,225))
        text.SetFont(font)     
        line = 'Copyright 2014 - Pranshu Gupta, Abhishek Jain, Rhythm Das.'
        text = wx.StaticText(panel, -1, line, (35, 700))
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        text.SetForegroundColour((0,0,128))
        text.SetFont(font)


    def dome(self, event):
        #Registering the player
        textbox = wx.TextEntryDialog(None,"First Player gets the black stone", ' New Player')
        if textbox.ShowModal() == wx.ID_OK:
            Name1 = textbox.GetValue()
            textbox = wx.TextEntryDialog(None,"Second Player gets the white stone", ' New Player')
            if textbox.ShowModal() == wx.ID_OK:
                Name2 = textbox.GetValue()
            else:
                return
        else:
            return
        renju.twoply(self, event, Name1, Name2)

    #the two player game
    def twoply(self, event, Name1, Name2):
        fread = open('theme.txt', 'r')
        default = fread.readline()
        fread.close()
        bif = default
        bsif = "noir.png"
        wsif = "blanc.png"
        i_icon = "icon.png"        
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        #setting the screen to 640 x 640 resolution
        screen = pygame.display.set_mode((640,640),0,32)
        #loading the background and stone images
        background = pygame.image.load(bif).convert()
        black = pygame.image.load(bsif).convert_alpha()
        white = pygame.image.load(wsif).convert_alpha()
        pygame.display.set_caption(str(Name1)+' vs '+str(Name2))
        blacks = []
        whites = []
        #loading the initial screen
        count = 1
        blacks.append((300,300))
        screen.blit(background,(0,0))
        screen.blit(black,(300,300))
        pygame.display.update()
        #the game loop
        while True:
            pos = [0,0]
            for event in pygame.event.get():
                #to quit when the user clicks the close button
                if event.type == QUIT:
                    pygame.quit()
                    #sys.exit()
                #we can detect the position where the player clicks and wether it's the black's turn or white's turn
                if event.type == MOUSEBUTTONDOWN:                   
                    pos  = list(event.pos)
                    flag = 1
                        
                    #finding the position at which the stones are to be placed
                    x = 20
                    while x<620:
                        if pos[0]>=x and pos[0]<x+40:
                            pos[0] = x
                            break
                        x = x+40
                    y = 20
                    while y<620:
                        if pos[1]>=y and pos[1]<y+40:
                            pos[1] = y
                            break
                        y = y+40
                    #checking if the move is valid    
                    j = 0
                    while j < len(whites):
                        if pos[0] == whites[j][0] and pos[1] == whites[j][1]:
                            flag = 0
                            break
                        j = j+1
                    j = 0
                    while j < len(blacks):
                        if pos[0] == blacks[j][0] and pos[1] == blacks[j][1]:
                            flag = 0
                            break
                        j = j+1
                    if pos[0]>620 or pos[0]<20 or pos[1]>620 or pos[1]<20:
                        flag=2
                        
                    if flag == 1:
                        count = count+1
                    #putting black or white stone according to the turns
                        if count%2 == 1:
                            
                            blacks.append((pos[0],pos[1]))
                            
                        elif count%2 == 0:
                        
                            whites.append((pos[0],pos[1]))
                                
                        i = 1
                        while i <= count:
                            if i%2 == 0:
                                screen.blit(white,whites[i/2 -1])
                                pygame.display.update()
                            else:
                                screen.blit(black,blacks[(i-1)/2 ])
                                pygame.display.update()
                            i = i+1

                stone = ""
                turn = []
                flag = 0
                if count%2 == 1:
                    stone = Name1
                    turn = blacks
                elif count % 2 == 0:
                    stone = Name2
                    turn = whites
                #checking after each step if any of the player has done five in a line
                I = 0
                while I < len(turn):
                    a = (turn[I][0],turn[I][1])
                    #searching for horizontal 4
                    n = 1
                    while n < 5:
                        if (a[0]+40*n, a[1])in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        b = (a[0]+40*5, a[1])
                        flag = 1
                        break
                    n= 1
                    while n < 5:
                        if (a[0]+40*n, a[1]+40*n)in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        flag = 1
                        b = (a[0]+40*5, a[1]+40*5)
                        break
                    n= 1
                    while n < 5:
                        if (a[0]+40*n, a[1]-40*n)in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        b = (a[0]+40*5, a[1]-40*5)
                        flag = 1
                        break
                    n= 1
                    while n < 5:
                        if (a[0], a[1]+40*n)in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        b = (a[0], a[1]+40*5)
                        flag = 1
                        break
                    I = I+1
                #declaring the winner
                if flag == 1:
                    pygame.time.delay(1000)
                    pygame.quit()
                    i_icon = 'icon.png'
                    if turn == blacks:
                        bif1 = 'win1.jpg'
                    if turn == whites:
                        bif1 = 'win2.jpg'
                    pygame.init()
                    pygame.display.set_icon(icon)
                    pygame.display.set_caption('! CONGRATULATIONS '+stone+' !')
                    screen = pygame.display.set_mode((600,300),0,32)
                    background = pygame.image.load(bif1).convert()
                    screen.blit(background,(0,0))
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                            if event.type == MOUSEBUTTONDOWN:
                                pos = list(event.pos)
                                if pos[0] > 400 and pos[0] < 580 and pos[1] > 200 and pos[1] < 240:
                                    pygame.quit()
                                    renju.twoply(self,event,Name1,Name2)
                                if pos[0] > 520 and pos[0] < 580 and pos[1] > 270 and pos[1] < 290:
                                    pygame.quit()
                                if pos[0] > 390 and pos[0] < 500 and pos[1] > 270 and pos[1] < 290:
                                    pygame.quit()
                                    renju.viewbrd(self,event,blacks,whites)
                        screen.blit(background,(0,0))                  
            screen.blit(background,(0,0))


    def about(self, event):
        i_icon = 'icon.png'
        bif2 = 'text.png'
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('ABOUT RENJU')
        screen = pygame.display.set_mode((600,300),0,32)
        background = pygame.image.load(bif2).convert()
        screen.blit(background,(0,0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            screen.blit(background,(0,0))


    def theme(self, event):
        i_icon = 'icon.png'
        bif3 = 'theme.jpg'
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('THEMES')
        screen = pygame.display.set_mode((600,300),0,32)
        background = pygame.image.load(bif3).convert()
        screen.blit(background,(0,0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    pos = list(event.pos)
                    if pos[0]>100 and pos[0]<140 and pos[1]>100 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid1.jpg')
                        fwrite.close()
                    if pos[0]>140 and pos[0]<180 and pos[1]>80 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid2.jpg')
                        fwrite.close()
                    if pos[0]>180 and pos[0]<220 and pos[1]>100 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid3.jpg')
                        fwrite.close()
                    if pos[0]>220 and pos[0]<260 and pos[1]>130 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid4.jpg')
                        fwrite.close()
                    if pos[0]>260 and pos[0]<300 and pos[1]>80 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid5.jpg')
                        fwrite.close()
                    if pos[0]>300 and pos[0]<340 and pos[1]>100 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid6.jpg')
                        fwrite.close()
                    if pos[0]>340 and pos[0]<380 and pos[1]>100 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid7.jpg')
                        fwrite.close()
                    if pos[0]>380 and pos[0]<420 and pos[1]>60 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid8.jpg')
                        fwrite.close()
                    if pos[0]>420 and pos[0]<460 and pos[1]>120 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid9.jpg')
                        fwrite.close()
                    if pos[0]>460 and pos[0]<500 and pos[1]>100 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid10.jpg')
                        fwrite.close()
                    if pos[0]>500 and pos[0]<540 and pos[1]>60 and pos[1]<260:
                        pygame.quit()
                        fwrite = open('theme.txt', 'w')
                        fwrite.writelines('grid11.jpg')
                        fwrite.close()
                        
            screen.blit(background,(0,0))

    def regist(self, event):
        #Registering the player
        textbox = wx.TextEntryDialog(None,"Your Name", ':) New Player')
        if textbox.ShowModal() == wx.ID_OK:
            Name = textbox.GetValue()
        else:
            return
        renju.oneply(self, event, Name)
    
    def oneply(self, event, Name):
        fread = open('theme.txt', 'r')
        default = fread.readline()
        fread.close()
        bif = default
        bsif = "noir.png"
        wsif = "blanc.png"
        i_icon = "icon.png"
        blacks = []
        whites = []
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        #setting the screen to 640 x 640 resolution
        screen = pygame.display.set_mode((640,640),0,32)
        #loading the background and stone images
        background = pygame.image.load(bif).convert()
        black = pygame.image.load(bsif).convert_alpha()
        white = pygame.image.load(wsif).convert_alpha()
        pygame.display.set_caption('Welcome ' + str(Name))
        #loading the initial screen
        count = 1
        blacks.append((300,300))
        screen.blit(background,(0,0))
        screen.blit(black,(300,300))
        pygame.display.update()
        #the game loop
        while True:
            pos = [0,0]
            for event in pygame.event.get():
                #to quit when the user clicks the close button
                if event.type == QUIT:
                    pygame.quit()
                    #sys.exit()
                #we can detect the position where the player clicks and wether it's the black's turn or white's turn
                if count%2 == 1:
                    if event.type == MOUSEBUTTONDOWN:                   
                        pos  = list(event.pos)
                        flag = 1
                        #finding the position at which the stones are to be placed
                        x = 20
                        while x<620:
                            if pos[0]>=x and pos[0]<x+40:
                               pos[0] = x
                               break
                            x = x+40
                        y = 20
                        while y<620:
                            if pos[1]>=y and pos[1]<y+40:
                               pos[1] = y
                               break
                            y = y+40
                        #checking if the move is valid    
                        j = 0
                        while j < len(whites):
                            if pos[0] == whites[j][0] and pos[1] == whites[j][1]:
                                flag = 0
                                break
                            j = j+1
                        j = 0
                        while j < len(blacks):
                            if pos[0] == blacks[j][0] and pos[1] == blacks[j][1]:
                                flag = 0
                                break
                            j = j+1
                        if pos[0]>620 or pos[0]<20 or pos[1]>620 or pos[1]<20:
                            flag=2


                        if flag == 1:
                            whites.append((pos[0],pos[1]))
                            i = 0
                            while i < len(whites):
                                screen.blit(white, whites[i] )
                                pygame.display.update()
                                i = i+1           
                            i = 0
                            while i < len(blacks):
                                screen.blit(black, blacks[i] )
                                pygame.display.update()
                                i = i+1

                            temp = 0
                            #checking after each step if any of the player has done five in a line
                            I = 0
                            while I < len(whites):
                                a = (whites[I][0],whites[I][1])
                                #searching for horizontal 4
                                n = 1
                                while n < 5:
                                    if (a[0]+40*n, a[1])in whites:
                                        n = n+1
                                    else:
                                        break
                                if n == 5:
                                    b = (a[0]+40*5, a[1])
                                    temp = 1
                                    break
                                n= 1
                                while n < 5:
                                    if (a[0]+40*n, a[1]+40*n)in whites:
                                        n = n+1
                                    else:
                                        break
                                if n == 5:
                                    temp = 1
                                    b = (a[0]+40*5, a[1]+40*5)
                                    break
                                n= 1
                                while n < 5:
                                    if (a[0]+40*n, a[1]-40*n)in whites:
                                        n = n+1
                                    else:
                                        break
                                if n == 5:
                                    b = (a[0]+40*5, a[1]-40*5)
                                    temp = 1
                                    break
                                n= 1
                                while n < 5:
                                    if (a[0], a[1]+40*n)in whites:
                                        n = n+1
                                    else:
                                        break
                                if n == 5:
                                    b = (a[0], a[1]+40*5)
                                    temp = 1
                                    break
                                I = I+1
                            #declaring the winner
                            if temp == 1:
                                renju.highscore(self,event)
                                pygame.time.delay(1000)
                                pygame.quit()
                                i_icon = 'icon.png'
                                bif4 = 'win.jpg'
                                pygame.init()
                                pygame.display.set_icon(icon)
                                pygame.display.set_caption('! CONGRATULATIONS '+Name+' !')
                                screen = pygame.display.set_mode((600,300),0,32)
                                background = pygame.image.load(bif4).convert()
                                screen.blit(background,(0,0))
                                pygame.display.update()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            pygame.quit()
                                        if event.type == MOUSEBUTTONDOWN:
                                            pos = list(event.pos)
                                            if pos[0] > 400 and pos[0] < 580 and pos[1] > 200 and pos[1] < 240:
                                                pygame.quit()
                                                renju.oneply(self,event,Name)
                                            if pos[0] > 520 and pos[0] < 580 and pos[1] > 270 and pos[1] < 290:
                                                pygame.quit()
                                            if pos[0] > 390 and pos[0] < 500 and pos[1] > 270 and pos[1] < 290:
                                                pygame.quit()
                                                renju.viewbrd(self,event,blacks,whites)
                                    screen.blit(background,(0,0))
                            count = count+1
                        
                if count%2 == 0:
                    algo.attack(blacks, whites, 0, 6, -1000, 1000)
                    #algo.attack(blacks,whites)
                    print count+1
                    pygame.display.update()
                    i = 0
                    while i < len(whites):
                        screen.blit(white, whites[i] )
                        pygame.display.update()
                        i = i+1           
                    i = 0
                    while i < len(blacks):
                        screen.blit(black, blacks[i] )
                        pygame.display.update()
                        i = i+1                

                    #checking after each step if any of the player has done five in a line
                    temp = 0
                    I = 0
                    while I < len(blacks):
                        a = (blacks[I][0],blacks[I][1])
                        #searching for horizontal 4
                        n = 1
                        while n < 5:
                            if (a[0]+40*n, a[1])in blacks:
                                n = n+1
                            else:
                                break
                        if n == 5:
                            b = (a[0]+40*5, a[1])
                            temp = 1
                            break
                        n= 1
                        while n < 5:
                            if (a[0]+40*n, a[1]+40*n)in blacks:
                                n = n+1
                            else:
                                break
                        if n == 5:
                            temp = 1
                            b = (a[0]+40*5, a[1]+40*5)
                            break
                        n= 1
                        while n < 5:
                            if (a[0]+40*n, a[1]-40*n)in blacks:
                                n = n+1
                            else:
                                break
                        if n == 5:
                            b = (a[0]+40*5, a[1]-40*5)
                            temp = 1
                            break
                        n= 1
                        while n < 5:
                            if (a[0], a[1]+40*n)in blacks:
                                n = n+1
                            else:
                                break
                        if n == 5:
                            b = (a[0], a[1]+40*5)
                            temp = 1
                            break
                        I = I+1
                    #declaring the winner
                    if temp == 1:
                        pygame.time.delay(1000)
                        pygame.quit()
                        i_icon = 'icon.png'
                        bif5 = 'lost.jpg'
                        pygame.init()
                        pygame.display.set_icon(icon)
                        pygame.display.set_caption(Name+' LOST')
                        screen = pygame.display.set_mode((600,300),0,32)
                        background = pygame.image.load(bif5).convert()
                        screen.blit(background,(0,0))
                        pygame.display.update()
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                if event.type == MOUSEBUTTONDOWN:
                                    pos = list(event.pos)
                                    if pos[0] > 400 and pos[0] < 580 and pos[1] > 200 and pos[1] < 240:
                                        pygame.quit()
                                        renju.oneply(self,event,Name)
                                    if pos[0] > 520 and pos[0] < 580 and pos[1] > 270 and pos[1] < 290:
                                        pygame.quit()
                                    if pos[0] > 390 and pos[0] < 500 and pos[1] > 270 and pos[1] < 290:
                                        pygame.quit()
                                        renju.viewbrd(self,event,blacks,whites)
                            screen.blit(background,(0,0))
                        pygame.quit()
                    count = count +1         
            screen.blit(background,(0,0))
        
    def closebutton(self, event):
        box = wx.MessageDialog(None, "Do you really want to exit?", ':(  EXIT !',wx.YES_NO)
        ans = box.ShowModal()
        box.Destroy
        if ans == 5103:
            self.Close(True)

    def highscore(self,event):
        return

    def viewbrd(self, event, blacks, whites):
        fread = open('theme.txt', 'r')
        default = fread.readline()
        fread.close()
        bif = default
        bsif = "noir.png"
        wsif = "blanc.png"
        i_icon = "icon.png"
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        #setting the screen to 640 x 640 resolution
        screen = pygame.display.set_mode((640,640),0,32)
        #loading the background and stone images
        background = pygame.image.load(bif).convert()
        black = pygame.image.load(bsif).convert_alpha()
        white = pygame.image.load(wsif).convert_alpha()
        pygame.display.set_caption('This what the board looked like after the last move.')
        screen.blit(background,(0,0))
        pygame.display.update()
        i = 0
        while i < len(whites):
            screen.blit(white, whites[i] )
            pygame.display.update()
            i = i+1           
        i = 0
        while i < len(blacks):
            screen.blit(black, blacks[i] )
            pygame.display.update()
            i = i+1
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            screen.blit(background,(0,0))    
        
if __name__ == '__main__':
    app = wx.App(False)
    frame =renju(parent = None, id = -1)
    frame.Show()
    app.MainLoop()

