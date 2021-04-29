#!/usr/bin/python3

import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('my.db')  
c = conn.cursor()

read_clients = pd.read_csv (r'./data.csv.old')
read_clients.to_sql('Datalogger', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'CLIENTS' 

# When reading the csv:
# - Place 'r' before the path string to read any special characters, such as '\'
# - Don't forget to put the file name at the end of the path + '.csv'
# - Before running the code, make sure that the column names in the CSV files match with the column names in the tables created and in the query below
# - If needed make sure that all the columns are in a TEXT format

