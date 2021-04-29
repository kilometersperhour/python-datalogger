#!/usr/bin/python3

import sqlite3
import pandas as pd
from pandas import DataFrame
import os, shutil

conn = sqlite3.connect('my.db')  
c = conn.cursor()

data_csv = r'./data.csv'
template_path = r'./legend.txt'
read_clients = pd.read_csv (data_csv)
read_clients.to_sql('Datalogger', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'Datalogger' 

os.remove(data_csv) # delete previously input data
shutil.copy2(template_path,data_csv) # make new csv for storage with same headers as previous
