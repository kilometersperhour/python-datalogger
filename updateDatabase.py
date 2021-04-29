#!/usr/bin/python3

import sqlite3
import pandas as pd
from pandas import DataFrame
import os, shutil

conn = sqlite3.connect('my.db')  
c = conn.cursor()

data_csv = r'./testLog.csv'
template_path = r'./legend.txt'
read_clients = pd.read_csv (data_csv)
read_clients.to_sql('Datalogger', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'Datalogger' 

os.remove(data_csv)
# template_fd = os.open(template_path, os.O_RDONLY)
# file_size = os.path.getsize(template_path)
# duplicate_fd = os.open(data_csv, os.O_RDWR | os.O_CREAT)
# os.sendfile(template_fd,duplicate_fd, 0, file_size) # offset is 0
shutil.copy2(template_path,data_csv)
# print(os.read(template_fd,os.path.getsize(template_path)))
# print(template_path,os.path.getsize(template_path))
