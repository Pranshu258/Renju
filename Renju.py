import wx
import algo
class renju(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id, 'RENJU', size = (1306,768))
        panel = wx.Panel(self)

        
        #the new game two player button
        pic = wx.Image("twoplayer.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic, pos = (335, 140))
        self.Bind(wx.EVT_BUTTON, self.dome, self.button)
        self.button.SetDefault()
        
        #the quit game button
        pic1 = wx.Image("quit.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic1, pos = (1180, 640))
        self.Bind(wx.EVT_BUTTON, self.closebutton, self.button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        self.button.SetDefault()

        #the about renju button
        pic3 = wx.Image("aboutrenju.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic3, pos = (945, 140))
        self.Bind(wx.EVT_BUTTON, self.about, self.button)
        self.button.SetDefault()

        #the one player button
        pic4 = wx.Image("oneplayer.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic4, pos = (30, 140))
        self.Bind(wx.EVT_BUTTON, self.oneply, self.button)
        self.button.SetDefault()

        #the themes button
        pic5 = wx.Image("themes.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic5, pos = (640, 140))
        self.Bind(wx.EVT_BUTTON, self.theme, self.button)
        self.button.SetDefault()

        #static text
        text = wx.StaticText(panel, -1, "RENJU - FIVE IN A LINE", (30, 10))
        font = wx.Font(72, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
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

        line = 'build 2.1'
        text = wx.StaticText(panel, -1, line, (37, 100))
        font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        text.SetForegroundColour((128,128,128))
        text.SetFont(font)          

    #the two player game
    def dome(self, event):
        fread = open('theme.txt', 'r')
        default = fread.readline()
        fread.close()
        bif = default
        bsif = "noir.png"
        wsif = "blanc.png"
        i_icon = "icon.png"
        err = 'error.png'
        #importing the libraries
        import pygame, sys
        from pygame.locals import *
        #Registering the player
        textbox = wx.TextEntryDialog(None,"First Player gets the black stone", ':) New Player', "First Player's name ")
        if textbox.ShowModal() == wx.ID_OK:
            Name1 = textbox.GetValue()
            textbox = wx.TextEntryDialog(None,"Second Player gets the white stone", ':) New Player', "Second Player's name ")
            if textbox.ShowModal() == wx.ID_OK:
                Name2 = textbox.GetValue()
            else:
                return
        else:
            return
        
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        #setting the screen to 640 x 640 resolution
        screen = pygame.display.set_mode((640,640),0,32)
        #loading the background and stone images
        background = pygame.image.load(bif).convert()
        black = pygame.image.load(bsif).convert_alpha()
        white = pygame.image.load(wsif).convert_alpha()
        error = pygame.image.load(err).convert_alpha()
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
                    if flag == 0:
                        screen.blit(error, (0,200))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        screen.blit(background,(0,0))
                        i = 1
                        while i <= count:
                            if i%2 == 0:
                                screen.blit(white,whites[i/2 -1])
                                pygame.display.update()
                            else:
                                screen.blit(black,blacks[(i-1)/2 ])
                                pygame.display.update()
                            i = i+1
                        
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
                    bif1 = 'win.jpg'
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
                        screen.blit(background,(0,0))
                    
                  
            screen.blit(background,(0,0))

    def about(self, event):
        i_icon = 'icon.png'
        bif2 = 'text.jpg'
        import pygame, sys
        from pygame.locals import *
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
        import pygame, sys
        from pygame.locals import *
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('THEMES')
        screen = pygame.display.set_mode((680,720),0,32)
        background = pygame.image.load(bif3).convert()
        screen.blit(background,(0,0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    pos = list(event.pos)
                    if pos[0]>0 and pos[0]<680 and pos[1]>0 and pos[1]<720:
                        if pos[1]>20 and pos[1]<220:
                            if pos[0]>20 and pos[0]<220:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid1.jpg')
                                fwrite.close()
                            if pos[0]>240 and pos[0]<440:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid2.jpg')
                                fwrite.close()
                            if pos[0]>460 and pos[0]<660:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid3.jpg')
                                fwrite.close()
                        if pos[1]>240 and pos[1]<440:
                            if pos[0]>20 and pos[0]<220:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid4.jpg')
                                fwrite.close()
                            if pos[0]>240 and pos[0]<440:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid5.jpg')
                                fwrite.close()
                            if pos[0]>460 and pos[0]<660:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid6.jpg')
                                fwrite.close()
                        if pos[1]>460 and pos[1]<660:
                            if pos[0]>20 and pos[0]<220:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid7.jpg')
                                fwrite.close()
                            if pos[0]>240 and pos[0]<440:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid8.jpg')
                                fwrite.close()
                            if pos[0]>460 and pos[0]<660:
                                pygame.quit()
                                fwrite = open('theme.txt', 'w')
                                fwrite.writelines('grid9.jpg')
                                fwrite.close()
            screen.blit(background,(0,0))

    def oneply(self, event):
        fread = open('theme.txt', 'r')
        default = fread.readline()
        fread.close()
        bif = default
        bsif = "noir.png"
        wsif = "blanc.png"
        i_icon = "icon.png"
        err = 'error.png'
        #importing the libraries
        import pygame, sys
        from pygame.locals import *
        #Registering the player
        textbox = wx.TextEntryDialog(None,"Your Name", ':) New Player', 'Enter your name here')
        if textbox.ShowModal() == wx.ID_OK:
            Name = textbox.GetValue()
        else:
            return
        pygame.init()
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        #setting the screen to 640 x 640 resolution
        screen = pygame.display.set_mode((640,640),0,32)
        #loading the background and stone images
        background = pygame.image.load(bif).convert()
        black = pygame.image.load(bsif).convert_alpha()
        white = pygame.image.load(wsif).convert_alpha()
        error = pygame.image.load(err).convert_alpha()
        pygame.display.set_caption('Welcome ' + str(Name))
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

                        if flag == 0:
                            screen.blit(error, (0,200))
                            pygame.display.update()
                            pygame.time.delay(1500)
                            screen.blit(background,(0,0))
                            i = 1
                            while i <= count:
                                if i%2 == 0:
                                    screen.blit(white,whites[i/2 -1])
                                    pygame.display.update()
                                else:
                                    screen.blit(black,blacks[(i-1)/2 ])
                                    pygame.display.update()
                                i = i+1

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
                                    screen.blit(background,(0,0))
                            count = count+1
                        
                if count%2 == 0:
                    algo.minmax(blacks, whites, 0, 4, -1000, 1000)
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
            
    def closewindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame =renju(parent = None, id = -1)
    frame.Show()
    app.MainLoop()

