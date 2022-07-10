import os
import glob
import time
from datetime import datetime
import csv
import RPi.GPIO as GPIO

GPIO_PIN_NUMBER=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

file = open("../ds18B20.csv", "w", newline="")
csv = csv.writer(file)
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        timestamp = datetime.now()
        print( "Temp C: {}    Temp F: {}    Time: {}".format(temp_c, temp_f, timestamp))
        return temp_c, temp_f, timestamp

csv.writerow(["temp_c", "temp_f", "timestamp"])

run = True
while run:
    import test_controller as controller
    import test2_controller as controller2

    try:
        # Print the values to the serial port
        temp_c, temp_f, timestamp = read_temp()
        csv.writerow([temp_c, temp_f, timestamp])
        if (temp_c < 21):
            print('Light blinking RGB')
            print("red light")
            controller.cleanUp()
            controller2.pinOn(21)
            controller.cycleColors()
            controller.cycleColors()
            controller.cycleColors()
            controller.cycleColors()

        if (temp_c >= 21):
            print("green light")
            controller2.cleanUp()
            controller2.pinOn(23)

        
    
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        raise error

    time.sleep(2.0)
