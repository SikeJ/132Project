import Tkinter as tk
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
    def __init__(self, placement, value = 0):
        self.placement = ""
        self.value = value


# Set up the GPIO pins for each photoresistor, and the two buttons that control the lazer
# Measure the average value of each photoresistor and set that as a set point
print ("Tyler's class")
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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
    while True:
        # These continuously update each Photoresistor object their light value from the array
        # in an infinite loop.
        topleft.value = pr1.value
        topmid.value = pr2.value
        topright.value = pr3.value
        midleft.value = pr4.value
        bullseye.value = pr5.value
        midright.value = pr6.value
        btmleft.value = pr7.value
        btmmid.value = pr8.value

        # Just print statements for each for Tyler's testing purposes. 
        print('Pin 1: ', topleft.value)
        print('Pin 2: ', topmid.value)
        print('Pin 3: ', topright.value)
        print('Pin 4: ', midleft.value)
        print('Pin 5: ', bullseye.value)
        print('Pin 6: ', midright.value)
        print('Pin 7: ', btmleft.value)
        print('Pin 8: ', btmmid.value)
        sleep(1)

        # Creates the array with all Photoresistor objects. 
        Array = [topleft, topmid, topright, midleft, bullseye, midright, btmleft, btmmid]

        return Array


# Array diagram
#  pr1----pr2----pr3
#  pr4----pr5----pr6   pr5 = bullseye
#  p7-----pr8-------



def Calculations(Array):
    pass



def GUI(Coords):
    pass


try:
    
    array = Reading()

except KeyboardInterrupt:
    print array
    GPIO.cleanup()





