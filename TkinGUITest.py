from Tkinter import *



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480



class Game(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

    def setUpGui(self):
        self.pack(fill = BOTH, expand = 1)

        img = None
        

        Game.image = Label(self, width = 600, image = img)
        Game.image.img = img
        Game.image.pack(side = LEFT, anchor = W, fill = Y)
        Game.image.pack_propagate(False)

        
        text_frame = Frame(self, width = WIDTH/2, height = HEIGHT/4, image = img)
        Game.text = Text(text_frame, bg = "red", state = DISABLED)
        Game.text.pack(fill = BOTH, expand = 1)
        text_frame.pack(side = TOP, anchor = NW)
        text_frame.pack_propagate(False)

        text_frame = Frame(self, width = WIDTH/2, height = 3*HEIGHT/4, image = img)
        Game.text = Text(text_frame, bg = "blue", state = DISABLED)
        Game.text.pack(fill = BOTH, expand = 1)
        text_frame.pack(side = RIGHT, fill = Y)
        text_frame.pack_propagate(False)

    def setPicture(self):

        Game.img = PhotoImage(file = "TargetPractice.gif")
        Game.image.config(image = Game.img)
        Game.image.image = Game.img


WIDTH = 800
HEIGHT = 480
window = Tk()

window.title("testing 123")

g = Game(window)

g.setUpGui()
g.setPicture()

window.mainloop()
