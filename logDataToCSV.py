#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: logDataToCSV.py
# Purpose: Collect data from four sensors and save as CSV file for later storage in database

import serial, string 		# for reading serial data from photoresistor
import csv, time 		# for saving to csv, + datestamps
import board, adafruit_ahtx0	# i2c imports from Adafruit example code for AHTx0

filename = "data.csv"
log_interval = 5

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)



while True:
#	print("\nTemperature: %0.1f C" % sensor.temperature)
#	print("Humidity: %0.1f %%" % sensor.relative_humidity)
	time_now = time.time()
	ambient_light = 4096

	try:
		with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
			ser.write(b'o')						# write a line to return a line
			ser_bytes = ser.readline()				# read a line
			ambient_light = ser_bytes.decode("utf-8","strict").rstrip()	# store what was read (0 - 4095)

		with open(f"{filename}","a") as myfile:
			writer = csv.writer(myfile,delimiter=",")
			newrow = [time_now,"%0.1f" % sensor.temperature,"%0.1f" % sensor.relative_humidity,ambient_light,0]
			writer.writerow(newrow)
			print(newrow)
	except:
		print("KeyboardInterrupt\n")
		break

	time_elapsed = time.time() - time_now	
	
	t = log_interval - time_elapsed 

	if t > 0 and t <= log_interval:
		time.sleep(t)

