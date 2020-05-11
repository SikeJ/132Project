import Tkinter as tk

#globally sets the window and ball size and number of balls
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
BALL_SIZE = 20
NUMBER = 100


#globally sets the colors to be used inside of the pygame window
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 255)
YELLOW = (255, 255, 0)

BUTTON = (165, 234, 45)


#sets starting coords for the lazer pointer
START_X = (SCREEN_WIDTH - 200) / 2
START_Y = (SCREEN_HEIGHT) / 2


##class GUI (Frame):
##
##    def __init__(self, parent):
##        Frame.__init__(self, parent)
##
##
##    def setupGUI (self):
##
##        #sets up the animation and buttons
##        pass


class Pointer(object):

    def __init__(self, canvas, x = 0, y = 0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x2 = x + 2*BALL_SIZE
        self.y2 = y + 2*BALL_SIZE
        self.id = canvas.create_oval(x, y, self.x2, self.y2, fill = "purple")
        self.dx = 1
        self.dy = 0
        

    #acessors and mutators
    @property
    def x (self):
        return self._x

    @x.setter
    def x (self, x):
        self._x = x

    @property
    def y (self):
        return self._y

    @y.setter
    def y (self, y):
        self._y = y

    @property
    def dx (self):
        return self._dx

    @dx.setter
    def dx (self, dx):
        self._dx = dx

    @property
    def dy (self):
        return self._dy

    @dy.setter
    def dy (self, dy):
        self._dy = dy

    def move(self, other):
        
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        x3, y3, x4, y4 = self.canvas.bbox(other.id)

#        while x1 != x3 and y1 != y3:

        if x1 > x3:
            self.dx = -1

        elif x1 < x3:
            self.dx = 1

        if y1 > y3:
            self.dy = -1

        elif y1 < y3:
            self.dy = 1

        self.canvas.move(self.id, self.dx, self.dy)
        
##        
##        if x2 > x4:
##            self.dx = -2
##            
##        if x1 < 0:
##            self.dx = 2
##
##        self.canvas.move(self.id, self.dx, self.dy)


class App(object):

    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)

        bg = tk.PhotoImage(file = "TargetPractice.gif")
        self.canvas.bg = bg
        self.canvas.create_image (SCREEN_WIDTH/2, SCREEN_HEIGHT/2, image = bg)

        self.coords = [Pointer(self.canvas, 10, 20), Pointer(self.canvas, 80, 120), Pointer(self.canvas, 300, 240)]

        self.canvas.pack()
        self.master.after(0, self.animation)

    def animation(self):
        
        point = Pointer(self.canvas, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        for coords in self.coords:
            #while coords.x != point.x and coords.y != point.y:
            coords.move(coords)
            
        self.master.after(10,self.animation)


root = tk.Tk()


app = App(root)
root.mainloop()
        
