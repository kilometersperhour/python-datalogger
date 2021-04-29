# datalogger

ATTENTION: Run ./run.py to update the webserver's images.

A datalogger is used to provide sensor data for display. The sensor data is presented graphically via a Linux-Apache2-Sqlite3 webserver stack.

Sensors include heat, humidity, ambient light, and a PIR (passive infrared) sensor.
This data is stored in a sqlite3 database each minute, and stored in a .csv file between database accesses. This minimizes database accessing (slow) and takes advantage of the comparatively faster operation of writing files to disk (between database accesses). In this case the database is stored on the same media as the .csv file will be written to, but the operation of writing to a database is more computationally intense than simple writes to disk, so this us the motivation for minimizing database operations. 
Data from the database is plotted using matplotlib, and the graphic created is saved to the website directory so that it can be displayed on the webpage. 
The displayed image is updated every minute, immediately following the database update.
