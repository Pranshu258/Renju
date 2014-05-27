import wx

class renju(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id, 'RENJU', size = (1306,768))
        panel = wx.Panel(self)
        
        status = self.CreateStatusBar()

        # create a background image on a wxPython panel
       

        try:
            # pick an image file you have in the working folder
            # you can load .jpg  .png  .bmp  or .gif files
            image_file = 'frame.jpg'
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
            
        except IOError:
            print "Image file %s not found" % imageFile
            raise SystemExit
 
        
        
        #the new game button
        pic = wx.Image("newgame.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic, pos = (1010, 0))
        self.Bind(wx.EVT_BUTTON, self.dome, self.button)
        self.button.SetDefault()
        
        #the quit game button
        pic1 = wx.Image("quit.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic1, pos = (1010, 650))
        self.Bind(wx.EVT_BUTTON, self.closebutton, self.button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        self.button.SetDefault()
       
        #the about renju button
        pic3 = wx.Image("renju.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic3, pos = (1010, 54))
        self.Bind(wx.EVT_BUTTON, self.about, self.button)
        self.button.SetDefault()
        
    def dome(self, event):
        
        
        bif = "grid.jpg"
        bsif = "noir.png"
        wsif = "blanc.png"
        i_icon = "icon.png"
        #importing the libraries
        import pygame, sys
        from pygame.locals import *
        #Registering the player
        textbox = wx.TextEntryDialog(None,"Name", ':) New Player', 'Enter your name here')
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
        pygame.display.set_caption('Welcome ' + str(Name))
        blacks = []
        whites = []
        #loading the initial screen
        count = 1
        print count
        blacks.append((300,300))
        print 'appended to black (300,300)'
        screen.blit(background,(20,20))
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
                    print pos
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
                        
                    j = 0
                    while j < len(whites):
                        if pos[0] == whites[j][0] and pos[1] == whites[j][1]:
                            flag = 0
                            print flag
                            break
                        j = j+1
                    j = 0
                    while j < len(blacks):
                        if pos[0] == blacks[j][0] and pos[1] == blacks[j][1]:
                            flag = 0
                            print flag
                            break
                        j = j+1
                    if pos[0]>620 or pos[0]<20 or pos[1]>620 or pos[1]<20:
                        flag=0
                    if flag == 1:
                        count = count+1
                        print count
                    #putting black or white stone according to the turns
                        if count%2 == 1:
                        
                            blacks.append((pos[0],pos[1]))
                            print 'appended to black ('+ str(pos[0]) + ', '+str(pos[1]) +')'
                        
                        elif count%2 == 0:
                    
                            whites.append((pos[0],pos[1]))
                            print 'appended to white ('+ str(pos[0]) + ', '+str(pos[1]) +')'
                            
                        i = 1
                        while i <= count:
                            if i%2 == 0:
                                screen.blit(white,whites[i/2 -1])
                                pygame.display.update()
                            else:
                                screen.blit(black,blacks[(i-1)/2 ])
                                pygame.display.update()

                            i = i+1
                    else:
                        wx.MessageBox('INVALID MOVE','ERROR 401',wx.OK)
                stone = ""
                turn = []
                flag = 0
                if count%2 == 1:
                    stone = "Black"
                    turn = blacks
                elif count % 2 == 0:
                    stone = "White"
                    turn = whites
                I = 0
                while I < len(turn):
                    a = (turn[I][0],turn[I][1])
                    n = 1
                    while n <= 5:
                        if (a[0]+40*n, a[1])in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        print stone + " wins the game\n"
                        wx.MessageBox(stone + " wins the game\n",'GAME OVER',wx.OK)
                        flag = 1
                        
                        break
                    n= 1
                    while n <= 5:
                        if (a[0]+40*n, a[1]+40*n)in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        print stone + " wins the game\n"
                        flag = 1
                        wx.MessageBox(stone + " wins the game\n",'GAME OVER',wx.OK)
                        break
                    n= 1
                    while n <= 5:
                        if (a[0]+40*n, a[1]-40*n)in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        print stone + " wins the game\n"
                        wx.MessageBox(stone + " wins the game\n",'GAME OVER',wx.OK)
                        flag = 1
                        break
                    n= 1
                    while n <= 5:
                        if (a[0], a[1]+40*n)in turn:
                            n = n+1
                        else:
                            break
                    if n == 5:
                        print stone + " wins the game\n"
                        wx.MessageBox(stone + " wins the game\n",'GAME OVER',wx.OK)
                        flag = 1
                        break
                    I = I+1

                if flag == 1:
                    pygame.quit()
                
                #sys.exit()
            screen.blit(background,(20,20))
            #screen.blit(black,(pos[0],pos[1]))
            #screen.blit(white,(120,120))
            #pygame.display.update()
            
    def about(self, event):
        box = wx.MessageDialog(None, "RENJU is played on the 225 intersections of 15 horizontal and 15 vertical lines. Two players, Black and White, move in turn by placing a stone of their own color on an empty intersection, henceforth called a square. Black starts the game. The player who first makes a line of five consecutive stones of his color (horizontally, vertically or diagonally) wins the game. The stones once placed on the board during the game never move again nor can they be captured. If the board is completely filled, and no one has five-in-a-row, the game is drawn.", 'About Renju'
,wx.OK)
        ans = box.ShowModal()
        box.Destroy
        
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

