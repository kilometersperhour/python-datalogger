#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: logDataToCSV.py
# Purpose: Collect data from four sensors and save as CSV file for later storage in database

import serial, string 		# for reading serial data from photoresistor
import csv, time 		# for saving to csv, + datestamps
import board, adafruit_ahtx0	# i2c imports from Adafruit example code for AHTx0

filename = "data.csv"

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
#	print("\nTemperature: %0.1f C" % sensor.temperature)
#	print("Humidity: %0.1f %%" % sensor.relative_humidity)
	try:
		with open(f"{filename}","a") as myfile:
			writer = csv.writer(myfile,delimiter=",")
			newrow = [time.time(),"%0.1f" % sensor.temperature,"%0.1f" % sensor.relative_humidity,0,0]
			writer.writerow(newrow)
			print(newrow)
	except:
		print("KeyboardInterrupt\n")
		break
	time.sleep(1)

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:

	while True:
		ser.write(b'o')						# write a line to return a line
		ser_bytes = ser.readline()				# read a line
		print(ser_bytes.decode("utf-8","strict").rstrip())	# pretty-print what was read
		time.sleep(1)						# repeat in one second

