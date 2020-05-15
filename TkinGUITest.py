from Tkinter import *



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480



class Game(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.attributes("-fullscreen", True)
        self.master = parent

    def setUpGui(self):
        self.pack(fill = BOTH, expand = 1)

        img = None
        

        Game.image = Label(self, image = img)
        Game.image.img = img
        Game.image.place(x = 0, y = 0)
        Game.image.pack_propagate(False)


        img = PhotoImage(file = "Buttons.gif")
        Game.buttons = Label(self, image = img)
        Game.buttons.img = img
        Game.buttons.place(x = 650, y = 0)
        Game.buttons.pack_propagate(False)
        
        b1 = Button(self.master, text="Show Lazer Again", command = testing)
        
        b1.place(x = 660, y = 90)

        b2 = Button(self.master, text="How to use", command = helping)
        b2.place(x = 680, y = 300)

        b3 = Button(self.master, text = "Show Pistol Chart", command = Pistol)
        b3.place(x = 665, y = 250)

        variable = StringVar(window)
        variable.set(1)

        w = OptionMenu(window, variable, 0.25, 0.5, 1, 2, 4, command= again)
        
        w.place(x = 700, y = 40)

        dropdown2 = StringVar(window)
        dropdown2.set(4)
        w2 = OptionMenu(window, dropdown2, 4, 5, 6, 7, 8, 9, 10, command = change)
        w2.place(x = 700, y = 170)

        b2 = Button(self.master, text = "Exit the Program", command = leave)
        b2.place(x = 665, y = 430)

        


    def setPicture(self, background):
        
        pictures = background + ".gif"
        Game.img = PhotoImage(file = pictures)
        Game.image.config(image = Game.img)
        Game.image.image = Game.img

    def Play(self):
        print "yes"

        self.master.after(1000,self.Play)




def testing():
    print "yes"

def again(test):
    print test

def leave():
    window.destroy()

def helping():
    g.setPicture("PistolChart")

def change(check):
    print check

def Pistol():
    g.setPicture("PistolChart2")

WIDTH = 800
HEIGHT = 480
window = Tk()



##try:
##    while True:
##        print "yes"
##
##except KeyboardInterrupt:
##    print "NO"

window.title("Aim Trainer")

g = Game(window)

g.setUpGui()
g.setPicture("Shoot")
g.Play()

window.mainloop()
