import Tkinter as tk
import RPi.GPIO as GPIO
from pygame import *
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from gpiozero import MCP3008
from time import sleep

class setupInputs(object):
    #set up the GPIO pins for each photoresistor, and the two buttons that control the lazer
    #measure the average value of each photoresistor and set that as a set point
    print "Tyler's class"
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    cs = digitalio.DigitalInOut(board.D5)

    mcp = MCP.MCP3008(spi, cs)

    r1 = AnalogIn(mcp, MCP.P0)
    r2 = AnalogIn(mcp, MCP.P1)
    r3 = AnalogIn(mcp, MCP.P2)
    r4 = AnalogIn(mcp, MCP.P3)
    r5 = AnalogIn(mcp, MCP.P4)
    r6 = AnalogIn(mcp, MCP.P5)
    r7 = AnalogIn(mcp, MCP.P6)
    r8 = AnalogIn(mcp, MCP.P7)

    Array = [r1, r2, r3, r4, r5, r6, r7, r8]
    array_Avg = sum(Array / 8)
    
class Graphics(canvas):
    #set up the GUI with pygame? or tkinter
    #use inputs from calculations to move the red dot around the screen based on values
    print "Jackson's class"
    pass


class Calculations(object):
    #use values measured from the photoresistors and setpoint to calculate where the lazer is
    print "Keith's class"
    pass


