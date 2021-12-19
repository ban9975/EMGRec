from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

x = []
y = []
index = count()

def animate(i):
	num = next(index)
	x.append(num)
	y.append(random.randint(0, 5))
	if num > 100:
		x.pop(0)
		y.pop(0)
	plt.cla()
	plt.plot(x, y)

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()