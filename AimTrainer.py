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

class setupInputs(object):
    # Set up the GPIO pins for each photoresistor, and the two buttons that control the lazer
    # Measure the average value of each photoresistor and set that as a set point
    print ("Tyler's class")
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # This is a class that creates each Photoresistor as an object. Each photoresistor
    # has a placement and a value. The placement is "topright, topmid, etc..."
    class Photoresistors(object):
        def __init__(self, placement, value = 0):
            self.placement = ""
            self.value = value

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

    # These create each Photoresistor object using the Photoresistors class. The names
    # designate where each sits on the physical array.
    topleft = Photoresistors("topleft")
    topmid = Photoresistors("topmid")
    topright = Photoresistors("topright")
    midleft = Photoresistors("midleft")
    bullseye = Photoresistors("bullseye")
    midright = Photoresistors("midright")
    btmleft = Photoresistors("btmleft")
    btmmid = Photoresistors("btmmid")

    # Creates the array with all Photoresistor objects. 
    Array = [topleft, topmid, topright, midleft, bullseye, midright, btmleft, btmmid]

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


    # Array diagram             # r5 = bullseye, s's are spaces between PRs
    #  r1--s1--r2--s2--r3
    #  -----------------
    #  s3--s4--s5--s6--s7
    #  -----------------
    #  r4--s7--r5--s8--r6
    #  -----------------
    #  s9--s10-s11-s12-s13
    #  -----------------
    #  r7--s14-r8--s14--
    

    # Array diagram
    #  pr1----pr2----pr3
    #  pr4----pr5----pr6   pr5 = bullseye
    #  p7-----pr8-------


class Graphics(canvas):
    # Set up the GUI with pygame? or tkinter
    # Use inputs from calculations to move the red dot around the screen based on values
    print ("Messing with Keith part 2")
    print ("Jackson's class")
    pass


class Calculations(object):
    # Use values measured from the photoresistors and setpoint to calculate where the lazer is

    tl = r1
    tm = r2
    tr = r3
    ml = r4
    be = r5
    mr = r6
    bl = r7
    bm = r8

    s1 = r1, r2
    s2 = r2, r3
    s3 = r1, r4
    s4 = r1, r5
    s4 = r2, r4
    s5 = r2, r5
    s6 = r2, r6
    s6 = r3, r5
    s7 = r3, r6
    
    Array.sort()
    closest_PR = Array[-1]
    2closest_PR = Array[-2]

    print "Keith's class"


    if (closest_PR >= 1000):
        hit = Array[-1]
        return hit
    
    elif:
        (closest_PR - 2closest_PR >= 250):
        hit = Array[-1],Array[-2]
        
    





