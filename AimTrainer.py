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
    print "Tyler's class"
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

    # Array diagram
    #  r1----r2----r3
    #  r4----r5----r6   r5 = bullseye
    #  r7----r8------
    
class Graphics(canvas):
    # Set up the GUI with pygame? or tkinter
    # Use inputs from calculations to move the red dot around the screen based on values
    print "Messing with Keith"
    print "Jackson's class"
    pass


class Calculations(object):
    # Use values measured from the photoresistors and setpoint to calculate where the lazer is
    print "Keith's class"
     for i in Array:
        if i >= 35000:
            return i

    # find highest one, then compare surrounding
    pass





#  for inputs a while True loop that is started and stopped by
