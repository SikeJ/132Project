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

    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    cs = digitalio.DigitalInOut(board.D5)

    mcp = MCP.MCP3008(spi, cs)

    #making this a function
    r1 = AnalogIn(mcp, MCP.P0)
    r2 = AnalogIn(mcp, MCP.P1)
    r3 = AnalogIn(mcp, MCP.P2)
    r4 = AnalogIn(mcp, MCP.P3)
    r5 = AnalogIn(mcp, MCP.P4)
    r6 = AnalogIn(mcp, MCP.P5)
    r7 = AnalogIn(mcp, MCP.P6)
    r8 = AnalogIn(mcp, MCP.P7)

    Array = [r1, r2, r3, r4, r5, r6, r7, r8]

    #setpoint needs to be its own function
    Setpoint = sum(Array / 8)

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

    if (closest_PR >= 1000):
        hit = Array[-1]
        return hit
    
    elif:
        (closest_PR - 2closest_PR >= 250):
        hit = Array[-1],Array[-2]
        
    





