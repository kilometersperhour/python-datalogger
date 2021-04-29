#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: logDataToCSV.py
# Purpose: Collect data from four sensors and save as CSV file for later storage in database

import serial, string 		# for reading serial data from photoresistor
import csv, time 		# for saving to csv, + datestamps
from datetime import datetime	# better datestamping
from datetime import timezone
import board, adafruit_ahtx0	# i2c imports from Adafruit example code for AHTx0
import wiringpi			# provides GPIO input interrupts

PIN_TO_SENSE = 17 # GPIO pin 17 will be used to measure input
filename = "testLog.csv" # will get added to database every minute
log_interval = 5 # every 5 seconds a new entry will be added

def gpio_edge():

	fetch_and_log()
	
def fetch_and_log():

	### Fetch

	time_unix = time.time()
	time_conventional = datetime.fromtimestamp(time_unix, tz=timezone.utc) 

	with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser: 	# fetch data from serial device
		ser.write(b'o')						# write a line to return a line
		ser_bytes = ser.readline()				# read a line
		ambient_light = ser_bytes.decode("utf-8","strict").rstrip()	# store what was read (0 - 4095)

	# I2C sensor data can be easily accessed with "sensor._______"

	if wiringpi.digitalRead(PIN_TO_SENSE):
		gpio_voltage = 3.3
	else:
		gpio_voltage = 0

	### Log

	with open(f"{filename}","a") as myfile:
		writer = csv.writer(myfile,delimiter=",")
		newrow = ["%0.1f" % time_now, "%0.1f" % sensor.temperature,"%0.1f" % sensor.relative_humidity, ambient_light, gpio_voltage]
		writer.writerow(newrow)
		print(f"{time_conventional} | {newrow}")

def elapse_remaining_interval():
	time_elapsed = time.time() - time_now	
	
	t = log_interval - time_elapsed 

	if t > 0 and t <= log_interval:
		time.sleep(t)

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

wiringpi.wiringPiSetupGpio() # initialize pins with GPIO-based pin numbering
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT) # set the GPIO PIN_TO_SENSE pin to INPUT
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_UP) # enable pull up resistor

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_BOTH, gpio_edge)

gpio_voltage = 0
newrow = [0,0,0,0,0]

while True:
	time_now = time.time()	
	fetch_and_log()
	elapse_remaining_interval()
