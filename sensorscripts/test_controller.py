import RPi.GPIO as GPIO
import time
red = 11
green = 13
blue = 15

def pinOn(color):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(color, GPIO.OUT)
    GPIO.output(color, True)

def pinOff(color):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(color, GPIO.OUT)
    GPIO.output(color, False)

def cycleColors():
    pinOn(red)
    time.sleep(0.2)
    pinOff(red)
    time.sleep(0.2)
    pinOn(green)
    time.sleep(0.2)
    pinOff(green)
    time.sleep(0.2)
    pinOn(blue)
    time.sleep(0.2)
    pinOff(blue)
    time.sleep(0.2)

def cleanUp():
    GPIO.cleanup()


