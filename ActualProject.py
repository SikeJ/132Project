from tkinter import *
import RPi.GPIO as GPIO
import pygame
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep

# Remember to use Python 3, specifically 3.5.5 but I"m sure any 3 will work.
# MCP3008 Library https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008

#globally sets the colors to be used inside of the pygame window
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

#sets the defaults for the starting pos, speed, and number of data points
START_X = (SCREEN_WIDTH - 200) / 2
START_Y = (SCREEN_HEIGHT) / 2
global speed
speed = 1
datapoints = 4
playagain = []

class Pointer(object):

    def __init__(self, x= 0, y= 0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

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


#sets up the class for the Tkinter GUI
class Game(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.attributes("-fullscreen", True)
        self.master = parent

    def setUpGui(self):
        self.pack(fill = BOTH, expand = 1)
        
        # sets up the two images for the Tkinter GUI and all of the buttons
        img = PhotoImage(file = "TargetPractice.gif")
        Game.image = Label(self, image = img)
        Game.image.img = img
        Game.image.place(x = 0, y = 0)
        Game.image.pack_propagate(False)

        img = PhotoImage(file = "Buttons.gif")
        Game.buttons = Label(self, image = img)
        Game.buttons.img = img
        Game.buttons.place(x = 650, y = 0)
        Game.buttons.pack_propagate(False)
        
        # button clicked to show the last animation
        b1 = Button(self.master, text="Show Laser Again", command = ShowAgain)        
        b1.place(x = 660, y = 100)

        # button that shows how to hold a pistol
        b2 = Button(self.master, text="How to Hold", command = Help)
        b2.place(x = 680, y = 300)

        # button that shows the total Pistol Chart
        b3 = Button(self.master, text = "Show Pistol Chart", command = Pistol)
        b3.place(x = 665, y = 250)

        # button that shows the proper stance
        b4 = Button(self.master, text = "How to Stand", command = Stance)
        b4.place(x = 680, y = 350)

        # a dropdown list to determine how many data points are going to be collected
        dropdown2 = StringVar(window)
        dropdown2.set(4)
        w2 = OptionMenu(window, dropdown2, 4, 5, 6, 7, 8, 9, 10, command = DataPoints)
        w2.place(x = 700, y = 170)
        
        # a drop down list to determine the speed of the animation
        variable = StringVar(window)
        variable.set(1)
        w = OptionMenu(window, variable, 0.25, 0.5, 1, 2, 4, command= Speed)        
        w.place(x = 700, y = 40)
        
        # button to quit the program
        b2 = Button(self.master, text = "Exit the Program", command = leave)
        b2.place(x = 665, y = 430)

    def setPicture(self, background):
        
        pictures = background + ".gif"
        Game.img = PhotoImage(file = pictures)
        Game.image.config(image = Game.img)
        Game.image.image = Game.img

    def Play(self):
        print("Something")
        array = []
        #reads the values and stores them in an array
        array.append(Reading())

        if max(array[0]) > 5000:
            i = 0
            print("Before")
            while (i < (datapoints)):
                array.append(Reading())
                i += 1
            #calculates the coords the lazer will go too
            calcs = Calculations(array)
            global playagain
            playagain = calcs

            #moves the laser to each point that was calculated
            for calc in calcs:
                point = Pointer(calc[0], calc[1])
                display = Pygame(point)
                sleep(.25)

               
            print (array)
            print (calcs)
            #quits pygame
            PygameQ()

        self.master.after(1000,self.Play)

#functions that set the background picture to the correct picture when buttons are pressed
def Help():
    g.setPicture("grip")

def Stance():
    g.setPicture("standing")


def Pistol(point):
    g.setPicture("PistolChart2")
    r = 5
    create_oval(point.x - r, point.y - r,\
                                 point.x + r, point.y + r,\
                                 outline = "magenta", fill = "magenta")


    



#sets the function that are called when the buttons are pressed
def ShowAgain():
    global array
    global playagain
    print("Show Again")
    for calc in playagain:
        point = Pointer(calc[0], calc[1])
        display = Pygame(point)
        sleep(.25)
    print(playagain)
    PygameQ()
        
    #print ("this button works, but need to implement the showagain feature")

def Speed(value):
    global speed
    speed = value
    #print("the speed of the thing should have changed")

def DataPoints(value):
    datapoints = value

def leave():
    window.destroy()
        

#create a function that reads the values at each photoresistor
def Reading():
    
    lists = []
    done = False
            
    # These continuously update each Photoresistor object their light value from the array
    # in an infinite loop.
    topleft = pr1.value
    topmid = pr2.value
    topright = pr3.value
    midleft = pr4.value
    bullseye = pr5.value
    midright = pr6.value
    btmleft = pr7.value
    btmmid = pr8.value

    Array = [topleft, topmid, topright, midleft, bullseye, midright, btmleft, btmmid]        
        
    # Just print statements for each for Tyler's testing purposes. 
    print('Pin 1: ', topleft)
    print('Pin 2: ', topmid)
    print('Pin 3: ', topright)
    print('Pin 4: ', midleft)
    print('Pin 5: ', bullseye)
    print('Pin 6: ', midright)
    print('Pin 7: ', btmleft)
    print('Pin 8: ', btmmid)
    sleep(.25)

    return Array


# Array diagram
#  pr1----pr2----pr3
#  pr4----pr5----pr6   pr5 = bullseye
#  pr7-----pr8-------



def Calculations(Array):
    x = 0
    y = 0
    coords = []
    #print("Something2")
    
    #takes the photoresistor values and adds them to get the final point
    for resist in Array:
        g.setPicture("loading")
        for i in range(resist[0]):
            x -= .01
            y -= .01

        for i in range(resist[3]):
            x -= .01

        for i in range(resist[6]):
            x -= .01
            y += .01

        for i in range(resist[1]):
            y -= .01

        for i in range(resist[7]):
            y += .01

        for i in range(resist[2]):
            x += .02
            y -= .01

        for i in range(resist[5]):
            x += .01

        if resist[4] == max(resist):
            x = 0
            y = 0
  
        coords.append([int(x), int(y)])
        
    return coords

#sets a function to quit pygame
def PygameQ():
    pygame.quit()
    
def Pygame(point):
    pygame.init()

    #sets up screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Aim Trainer")
    bg = pygame.image.load("TargetPractice.gif")

    #sets the screen refresh rate time
    clock = pygame.time.Clock()

    #gives the starting point for the 'lazer' everytime

    done = False

    #range checks the provided coords, to not get a value that's outside of the box
    point.x += 300
    point.y += 240
    
    if point.x < 150:
        point.x = 150

    elif point.x > 450:
        point.x = 450

    if point.y < 120:
            point.y = 120

    elif point.y > 360:
            point.y = 360

    #calculates how much the x and y need to change to get there in a particular time
    changex = (pos.x - point.x) / (speed * 60)
    changey = (pos.y - point.y) / (speed * 60)

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pos.x == point.x and pos.y == point.y:
            done = True
        

        if pos.x - point.x == 0:
            pos.dx = 0
        
        elif pos.x - point.x > 0:
            pos.dx = -1 

            if pos.y - point.y == 0:
                pos.dy = 0
            
            elif pos.y - point.y > 0:
                pos.dy = -1 

            elif pos.y - point.y < 0:
                pos.dy = 1 
            

        elif pos.x - point.x < 0:
            pos.dx = 1 

            if pos.y - point.y == 0:
                pos.dy = 0

            if pos.y - point.y > 0:
                pos.dy = -1

            elif pos.y - point.y < 0:
                pos.dy = 1

        pos.x += pos.dx
        pos.y += pos.dy

        #draws the screen background white, and draws the background of the target
        screen.fill(WHITE)
        screen.blit(bg, [0,0])

        #draws the location of the lazer pointer as it is moving
        pygame.draw.circle(screen, RED, [int(pos.x),int(pos.y)], 20)
            
        #locks the screen FPS at 60 and draws the display on the screen
        global speed
        clock.tick(20 * speed)
        pygame.display.flip()






###############################################
#main part of program
##################################################

# These just setup inputs and outputs for the Pi to communicate with the MCP3008 chip.
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

# These give each channel from the MCP3008 a variable. "pr" = Photoresistor
pr1 = AnalogIn(mcp, MCP.P0)
pr2 = AnalogIn(mcp, MCP.P1)
pr3 = AnalogIn(mcp, MCP.P2)
pr4 = AnalogIn(mcp, MCP.P3)
pr5 = AnalogIn(mcp, MCP.P4)
pr6 = AnalogIn(mcp, MCP.P5)
pr7 = AnalogIn(mcp, MCP.P6)
pr8 = AnalogIn(mcp, MCP.P7)

pos = Pointer(START_X, START_Y)
        
#starts the Tkinter GUI
window = Tk()
window.title("AimTrainer")

g = Game(window)
g.setUpGui()
g.setPicture("shoot")
g.Play()
window.mainloop()
#starts a endless loop checking the values




