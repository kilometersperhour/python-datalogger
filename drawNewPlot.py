#!/usr/bin/python3

# Miles Martin - ECE 331
# Project 3 - Datalogger
# Program: makeNewPlot.py
# Purpose: Draw new plots for the website

import sqlite3, time, datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('my.db')
c = conn.cursor()

columns = ('Unix_Time','Temperature','Relative_Humidity','Ambient_Light','PIR_Voltage')
