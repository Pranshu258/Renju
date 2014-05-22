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
        #the newplayer button
        pic2 = wx.Image("newplayer.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic2, pos = (1010, 54))
        self.Bind(wx.EVT_BUTTON, self.newplayer, self.button)
        self.button.SetDefault()
        #the about renju button
        pic3 = wx.Image("renju.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, pic3, pos = (1010, 108))
        self.Bind(wx.EVT_BUTTON, self.about, self.button)
        self.button.SetDefault()
        
    def dome(self, event):
        
        
        bif = "grid.jpg"
        bsif = "blackstone.png"
        wsif = "whitestone.png"
        #importing the libraries
        import pygame, sys
        from pygame.locals import *

        pygame.init()
        #setting the screen to 640 x 640 resolution
        screen = pygame.display.set_mode((640,640),0,32)
        #loading the background and stone images
        background = pygame.image.load(bif).convert()
        black = pygame.image.load(bsif).convert_alpha()
        white = pygame.image.load(wsif).convert_alpha()
        pygame.display.set_caption('The RENJU window')
        blacks = []
        whites = []
       
        count = 0        
        #the game loop
        while True:
    
            for event in pygame.event.get():
                #to quit when the user clicks the close button
                if event.type == QUIT:
                    pygame.quit()
                    #sys.exit()
                #we can detect the position where the player clicks and wether it's the black's turn or white's turn
                if event.type == MOUSEBUTTONDOWN:                   
                    
                    print event.pos
                    count = count+1
                    if count%2 == 1:
                         blacks.append((event.pos[0],event.pos[1]))
                         print 'appended to black'
                    elif count%2 == 0:
                         whites.append((event.pos[0],event.pos[1]))
                         print 'appended to white'
                    print count

                   
                    
               #if five in a row:
               #if black:
                #    print "Black player won.\n"
                #if white:
                #    print "White player won.\n"
                #print 'GAME OVER  \n'
                
                #pygame.quit()
                #sys.exit()
            screen.blit(background,(20,20))
            screen.blit(black,(120,40))
            screen.blit(white,(120,120))
            pygame.display.update()
            
    def about(self, event):
        box = wx.MessageDialog(None, "RENJU", 'About Renju',wx.YES_NO)
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
    def newplayer(self, event):
        textbox = wx.TextEntryDialog(None,"Name", ':) New Player', 'Enter your name here')
        if textbox.ShowModal() == wx.ID_OK:
            Name = textbox.GetValue()

if __name__ == '__main__':
    app = wx.App(False)
    frame =renju(parent = None, id = -1)
    frame.Show()
    app.MainLoop()

