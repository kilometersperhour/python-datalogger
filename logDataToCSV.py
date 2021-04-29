#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: logDataToCSV.py
# Purpose: Collect data from four sensors and save as CSV file for later storage in database

#TODO: Still isn't reading anything. Fix that.

# import serial
# import time

# with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:

#	print('Writing...')
#	ser.write(b'poggers\n')		# write a line to return a line
#	print('Written. Reading...')
#	time.sleep(1)
#	ser_bytes = ser.readline()	# read a line
#	print('Read. Printing...')
#	print(ser_bytes)		# print what was read
#	time.sleep(2)			# repeat in two seconds

import serial, csv
import time
import board
import adafruit_ahtx0

filename = "t_h_data.csv"

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
