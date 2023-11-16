# Gaia
An intelligent environmental control system

I want to create an intelligent enviromental system that optimizes settings for the growth cycle of a particular living subject, for example a plant. The system will take readings from enviromental factors such as light, humidity in the air, the ratio of CO2 and O2, temperature, etc.. at every defined interval over the time of a specific plants growth. Given this dataset, I want to write artificial intelligence model to predict optimize percent yield, and reduce the amount of energy (kWh) used.

##

## Sensors
•	DS18B20 Temperature Sensor (°C).  
•	MIX8410 (O2 %).  
•	MH-Z14B NDIR  (CO2 ppm).  
•	TSL25911FN Ambient Light Sensor (Lux).  
•	GMP343 CO₂.  
•	LI-190 Quantum Sensor CO₂.  
•	DHT11 Temperature / Humidity (CO2 , %Humidity).  
  - DHT22 Temperature / Humidity (CO2 , %Humidity).  
•	CS215 Temperature / Humidity.  
•	M-LVTD Linear variable displacement transducer – Stem width - ?   

## Data Points: 
###Inputs
•	CO2.  
•	O2.  
•	Temperature.  
•	Humidity.  
•	H20 pH.  
•	Light Intensity.  
•	Light Frequency.  

###Outputs
<!-- •	Radiation.   -->
•	% Yield.  
• Energy (kWh).  
• Cost $.  

## Research:
•	Using Deep Learning to Predict Plant Growth and Yield in Greenhouse Environments   

## Equipment
•  3ft x 3ft x 59in grow tent
•  150Watt Full Spectrum L.E.D light

## Pinout

   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

POE:
TR01 (1) (2) TR00
TR03 (3) (4) TR02


## Market Research:
  Competition:
    •	https://aigrowlight.com/about-us/.  
    •	Existing Patent.  
![image](https://user-images.githubusercontent.com/45886361/151272973-74ecb4a9-f9fa-42de-85c3-1f1a4ef1ff91.png)
