#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('my.db')
c = conn.cursor()

c.execute('''CREATE TABLE Datalogger ([Unix_Time] real,[Temperature] real,[Relative_Humidity] real,[Ambient_Light] real,[PIR_Voltage] real)''')

conn.commit()
