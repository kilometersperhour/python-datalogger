#!/usr/bin/python3

import wiringpi
PIN_TO_SENSE = 17

def gpio_edge():
	if wiringpi.digitalRead(PIN_TO_SENSE):
		voltage = "HIGH"
	else:
		voltage = "LOW"
	print(f"Edge occurred. Voltage is {voltage}.")

wiringpi.wiringPiSetupGpio() # initialize pins with wiringPi numbering
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT) # wiringPi 0 (GPIO 17) is an input
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_UP) # set pull up resistor

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_BOTH, gpio_edge)

while True:
	wiringpi.delay(2000)
