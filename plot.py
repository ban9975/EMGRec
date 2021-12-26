from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

x = []
y = []
index = count()

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)
# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

def animate(i):
	num = next(index)
	x.append(num)
	y.append(chan.value)
	if num > 100:
		x.pop(0)
		y.pop(0)
	plt.cla()
	plt.plot(x, y)


ani = FuncAnimation(plt.gcf(), animate, interval=10)
plt.tight_layout()
plt.show()
