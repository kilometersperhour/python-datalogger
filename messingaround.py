#!/usr/bin/python3

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Basic `AHTx0` example test
"""
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
			writer.writerow([time.time(),"%0.1f" % sensor.temperature,"%0.1f" % sensor.relative_humidity])
	except:
		print(f"Didn't write to {filename}\n")
		break
	time.sleep(1)
