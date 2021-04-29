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

conn = sqlite3.connect('my.db')
c = conn.cursor()

columns = ('Unix_Time','Temperature','Relative_Humidity','Ambient_Light','PIR_Voltage')
db_name = "Datalogger"
# referenced pythonprogramming.net

def read_from_db():
        c.execute('SELECT * FROM (?)',(Datalogger))
        data = c.fetchall()
        print(data)
        for row in data:
                print(row)

def graph_data(int col):
        c.execute('SELECT (?,?) FROM Datalogger', (columns[0] columns[col])
        data = c.fetchall()

        time = []
        values = []

        for row in data:
                dates.append(parser.parse(row[0]))
                values.append(row[1])

        plt.xlabel('%s' % columns[0])
        plt.ylabel('%s' % columns[col])

        plt.plot_date(dates,values,'-')
        plt.show

read_from_db()
c.close()
conn.close()
