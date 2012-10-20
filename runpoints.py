import led
import time
import math
from random import random
from array import *
import movingPixel

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"


colors = { "red"   : (1023,0,0),
	   "green" : (0,1023,0),
	   "blue"  : (0,0,1023) }


w=30
h=6
maxcol = 1023

tmp=led.frame(w,h)
leer=led.frame(w,h)





x=-1
y=-1

output=led.output()
map(lambda l: l.setColor(1023,1023,1023), leer.getAllPixel())
interval = 0.3
#Brightness Values
r = 20
g = 20
b = 20
pic1 = movingPixel.pixelPic([[(r,0,0) for i in range(h)] for j in range(w)], tmp, interval)
pic2 = movingPixel.pixelPic([[(0,g,0) for i in range(h)] for j in range(w)], tmp, interval)
pic3 = movingPixel.pixelPic([[(0,0,b) for i in range(h)] for j in range(w)], tmp, interval)
pic4 = movingPixel.pixelPic([[(r,g,0) for i in range(h)] for j in range(w)], tmp, interval)
pic5 = movingPixel.pixelPic([[(0,g,b) for i in range(h)] for j in range(w)], tmp, interval)
pic6 = movingPixel.pixelPic([[(r,0,b) for i in range(h)] for j in range(w)], tmp, interval)
pic7 = movingPixel.pixelPic([[(r,g,b) for i in range(h)] for j in range(w)], tmp, interval)
controller = movingPixel.controller([pic7, pic4, pic6, pic1, pic5, pic2, pic3])


while True:
	controller.loop()
	output.write(tmp)
	#time.sleep(0.005)
