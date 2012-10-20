import led
import time
import math
from random import random
from array import *

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"

w = 30
h = 6
maxcol = 1023

tmp = led.frame(w, h)
leer = led.frame(w, h)
x = -1
y = -1

output = led.output()
map(lambda l: l.setColor(1023, 1023, 1023), leer.getAllPixel())
t = 0

while True:
	if t > maxcol:
		t = 0
	for row in tmp.rows:
		for pt in row.leds:
			r = 0
			b = 0
			g = 0
			while(r + g + b < 1):
				if(  (int(random()*1000)) % 3 == 0):
					r = int(maxcol)
				elif((int(random()*1000)) % 3 == 1):
					g = int(maxcol)
				elif((int(random()*1000)) % 3 == 2):
					b = int(maxcol)
			pt.setColor(r,g,b)
			time.sleep(0.001)	
	
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	#time.sleep(0.05)
	t+=1
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())
