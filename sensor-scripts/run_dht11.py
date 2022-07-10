from datetime import datetime
import time
import board
import adafruit_dht
import csv

file = open("dht11.csv", "w", newline="")
csv = csv.writer(file)
dhtDevice = adafruit_dht.DHT11(board.D17, use_pulseio=False)

def dht11():
        temp_c = dhtDevice.temperature
        temp_f = temp_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        timestamp = datetime.now()
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}%    Time: {}".format(
                temp_f, temp_c, humidity, timestamp
            )
        )
        return temp_c, temp_f, humidity, timestamp
    

 
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
csv.writerow(["temp_c", "temp_f", "humidity", "timestamp"])
while True:
    try:
        # Print the values to the serial port
        temp_c, temp_f, humidity, timestamp = dht11()
        csv.writerow([temp_c,temp_f, humidity, timestamp])
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2.0)