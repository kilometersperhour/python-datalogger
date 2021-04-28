#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: logDataToCSV.py
# Purpose: Collect data from four sensors and save as CSV file for later storage in database

#TODO: Still isn't reading anything. Fix that.

import serial
import time

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:

	print('Writing...')
	ser.write(b'poggers\n')		# write a line to return a line
	print('Written. Reading...')
	time.sleep(1)
	ser_bytes = ser.readline()	# read a line
	print('Read. Printing...')
	print(ser_bytes)		# print what was read
	time.sleep(2)			# repeat in two seconds
