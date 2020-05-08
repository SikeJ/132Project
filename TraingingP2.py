import tkinter as tk
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



# This is a class that creates each Photoresistor as an object. Each photoresistor
# has a placement and a value. The placement is "topright, topmid, etc..."
class Photoresistors(object):
    def __init__(self, value = 0):
        self.value = value


# Set up the GPIO pins for each photoresistor, and the two buttons that control the lazer
# Measure the average value of each photoresistor and set that as a set point
##print ("Tyler's class")
##GPIO.setmode(GPIO.BOARD) 
##GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#globally sets the colors to be used inside of the pygame window
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 255)
YELLOW = (255, 255, 0)

BUTTON = (165, 234, 45)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

#sets starting coords for the lazer pointer
START_X = (SCREEN_WIDTH - 200) / 2
START_Y = (SCREEN_HEIGHT) / 2

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


pygame.init()

#sets up screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Aim Trainer")
bg = pygame.image.load("TargetPractice.gif")

#sets the screen refresh rate time
clock = pygame.time.Clock()



pos = Pointer(START_X, START_Y)



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



#create a function that reads the values at each photoresistor
def Reading():

    lists = []
    done = False
    while not done:

        #empty list
        
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


        #waits for a value to go over a threshold and collects each photoresistor data
        #and stores it into an array
        for value in Array:
            if value >= 5000:
                i = 0
                while i < 4:
                    topleft = pr1.value
                    topmid = pr2.value
                    topright = pr3.value
                    midleft = pr4.value
                    bullseye = pr5.value
                    midright = pr6.value
                    btmleft = pr7.value
                    btmmid = pr8.value

                    Array = [topleft, topmid, topright, midleft, bullseye, midright, btmleft, btmmid]
                    lists.append(Array)
                    
                    sleep (.5)
                    
                    i += 1

                Array = lists
                done = True
                break
                    
            
        # Just print statements for each for Tyler's testing purposes. 
        print('Pin 1: ', topleft)
        print('Pin 2: ', topmid)
        print('Pin 3: ', topright)
        print('Pin 4: ', midleft)
        print('Pin 5: ', bullseye)
        print('Pin 6: ', midright)
        print('Pin 7: ', btmleft)
        print('Pin 8: ', btmmid)
        sleep(1)

        # Creates the array with all Photoresistor objects. 
        

    return Array


# Array diagram
#  pr1----pr2----pr3
#  pr4----pr5----pr6   pr5 = bullseye
#  pr7-----pr8-------



def Calculations(Array):
    x = 0
    y = 0
    coords = []
    for resist in Array:
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
            y -= .01

        for i in range(resist[2]):
            x += .01
            y += .01

        for i in range(resist[5]):
            x += .01
  
        coords.append([int(x), int(y)])
    return coords



def GUI(point):
    done = False

    #range checks the provided coords, to not get a value that's outside of the box
   

    print(point.x)
    print(point.y) 


    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pos.x == point.x and pos.y == point.y:
            done = True

        if pos.x < 150:
            pos.x = 150

        elif pos.x > 450:
            pos.x = 150

        if pos.y < 120:
            pos.y = 120

        elif pos.y > 360:
            pos.y = 360

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

        


        screen.fill(WHITE)

        screen.blit(bg, [0,0])


        pygame.draw.circle(screen, RED, [int(pos.x),int(pos.y)], 20)

##        for yes in points:
##            pygame.draw.circle(screen, YELLOW, [yes.x,yes.y], 5)
            
        #makes the screen white, and draws the background picture,
        #then the picture of the pointer ontop of the background pic
        

        #adding button?
        pygame.draw.rect(screen, BUTTON, [650,60,100,50])

        #normal stuff
        #pygame.draw.circle(screen, RED, [45,203], 1)
        
        clock.tick(60)
        pygame.display.flip()



###############################################
#main part of program
##################################################
        
try:
    
    array = Reading()

    calcs = Calculations(array)

    for calc in calcs:
        point = Pointer(calc[0], calc[1])
        display = GUI(point)
        sleep(1)

       
    print (array)
    print (calcs)

    pygame.quit()

    
except KeyboardInterrupt:
   
    GPIO.cleanup()





