import sys
import csv
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

if len(sys.argv) >= 1:
	fileName = sys.argv[1] + '.csv'
else:
	fileName = 'output.csv'

if len(sys.argv) >= 2:
	duration = int(sys.argv[2])
else:
	# default collect data for 5 seconds
	duration = 5

start = time.time()
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chaUp = AnalogIn(ads, ADS.P0)
chaDown = AnalogIn(ads, ADS.P1)

with open(fileName, 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['up', 'down'])
	while time.time() - start < duration:
		writer.writerow([chaUp.value, chaDown.value])
