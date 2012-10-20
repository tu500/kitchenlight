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



w=30
h=6
maxcol = 1023

tmp=led.frame(w,h)
leer=led.frame(w,h)
x=-1
y=-1

output=led.output()
map(lambda l: l.setColor(1023,1023,1023), leer.getAllPixel())
t=0

while True:
	if t>maxcol:
		t=0
	for row in tmp.rows:
		i = 0
		for pt in row.leds:
			i += 1
			r = 0
			b = 0
			g = 0
			if (i < t) | ((w - i) < t):
				while (r + g + b) <= maxcol/3:	
					if(random() > 0.3):
						r = int(maxcol*random())
					if(random() > 0.3):	
						g = int(maxcol*random())		
					if(random() > 0.3):
						b = int(maxcol*random())
				if (r + g + b) > 2 * maxcol:
					r = int(r/3)
					g = int(g/3)
					b = int(b/3)
			pt.setColor(r,g,b)
			time.sleep(0.001)	
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	time.sleep(0.05)
	t+=1
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())
