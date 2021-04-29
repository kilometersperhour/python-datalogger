#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: captureSerial.py
# Purpose: Collect data from serial-port-based sensor and print to screen

import serial
import time
import string

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:

	while True:
		ser.write(b'o')						# write a line to return a line
		ser_bytes = ser.readline()				# read a line
		print(ser_bytes.decode("utf-8","strict").rstrip())	# pretty-print what was read
		time.sleep(1)						# repeat in one second

