import tkinter as tk
import RPi.GPIO as GPIO
from pygame import *
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
#  p7-----pr8-------



def Calculations(Array):
    x = 0
    y = 0
    coords = []
    for resist in Array:
        for i in range(resist[0]):
            x -= .01
            y += .01

        for i in range(resist[3]):
            x -= .01

        for i in range(resist[6]):
            x -= .01
            y -= .01

        for i in range(resist[1]):
            y += .01

        for i in range(resist[7]):
            y -= .01

        for i in range(resist[2]):
            x += .01
            y += .01

        for i in range(resist[5]):
            x += .01
  
        coords.append([x, y])
    return coords

def GUI(Coords):
    pass


try:
    
    array = Reading()

    calcs = Calculations(array)
    

    
    print (array)
    print (calcs)
except KeyboardInterrupt:
   
    GPIO.cleanup()





