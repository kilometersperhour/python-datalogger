#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: makeNewPlot.py
# Purpose: Draw new plots for the website

import sqlite3 
import time
import datetime 
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

# style.use('fivethirtyeight')

plt.savefig.format = "png"

conn = sqlite3.connect('my.db')
c = conn.cursor()

columns = ('Unix_Time','Temperature','Relative_Humidity','Ambient_Light','PIR_Voltage')
columns_units = ('Date, Hours','Degrees Celsius','Percentage','Unitless','Volts')
db_name = "Datalogger"

def graph_data(col):
	
	one_day_ago = (time.time() - 24*60*60) # 86400 seconds ago
	
	if col == 2:
		parameter = 17.5
		c.execute(f'SELECT {columns[0]},{columns[col]} FROM {db_name} WHERE {columns[col]} > {parameter} AND {columns[0]} > {one_day_ago};')
	else:
		parameter = 4096
		c.execute(f'SELECT {columns[0]},{columns[col]} FROM {db_name} WHERE {columns[col]} < {parameter} AND {columns[0]} > {one_day_ago};')
	
	data = c.fetchall()
	print(f"Data fetched for {columns[col]}")
	
	times = []
	values = []

	for row in data:
		times.append(row[0])
		values.append(row[1])
		
	for i in range(len(times)):	
		times[i] = datetime.datetime.fromtimestamp(times[i])	

	plt.clf()
	plt.xlabel('%s' % columns_units[0])
	plt.ylabel('%s' % columns_units[col])
#	plt.rcParams.update({'font.size': 12})
	plt.plot(times,values,color=(random.random(), random.random(), random.random())) # random color
	
	plt.title(f'{columns[col]} Over Time')
	plt.tight_layout()
	plt.xticks(rotation = 15)

	plt.savefig(f'/var/www/html/{columns[col]}.png')
	print(f'Saved /var/www/html/{columns[col]}.png')

for i in range(1,5):
	graph_data(i)
c.close()
conn.close()
