#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: makeNewPlot.py
# Purpose: Draw new plots for the website

import sqlite3, time, datetime, random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

style.use('fivethirtyeight')

plt.savefig.format = "png"

conn = sqlite3.connect('my.db')
c = conn.cursor()

columns = ('Unix_Time','Temperature','Relative_Humidity','Ambient_Light','PIR_Voltage')
db_name = "Datalogger"

def read_from_db():
	c.execute('SELECT * FROM %s;' % db_name)
	data = c.fetchall()
	print(data)
	for row in data:
		print(row)

def graph_data(col):
	if col == 2:
		parameter = 17.5
		c.execute(f'SELECT {columns[0]},{columns[col]} FROM {db_name} WHERE {columns[col]} > {parameter};')
	else:
		parameter = 4096
		c.execute(f'SELECT {columns[0]},{columns[col]} FROM {db_name} WHERE {columns[col]} < {parameter};')
	
	data = c.fetchall()

	time = []
	values = []

	for row in data:
		time.append(row[0])
		values.append(row[1])
		
	plt.xlabel('%s' % columns[0])
	plt.ylabel('%s' % columns[col])
	
	plt.clf()
	plt.plot(time,values,'-')
	plt.savefig(f'/var/www/html/{columns[col]}.png')

read_from_db()
graph_data(1)
graph_data(2)
graph_data(3)
graph_data(4)
c.close()
conn.close()
