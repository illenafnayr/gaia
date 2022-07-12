import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=17)
with open('data.csv', 'w') as file:

    while True:
        result = instance.read()
        if result.is_valid():
            file.write("{:s},{:d},{:f},{:d}\n".format(
                str(datetime.datetime.now()),
                result.temperature,
                ((result.temperature * 9/5)+32),
                result.humidity
            ))
time.sleep(1)