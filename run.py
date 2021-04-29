import os, time

while True:
	os.system("./updateDatabase.py")
	os.system("./drawNewPlot.py")
	i = 50
	while i != 0:
		print(i)
		time.sleep(1)
		i = i - 1
