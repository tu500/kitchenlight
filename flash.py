import led
import time
import math

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"



w=30
h=6

tmp=led.frame(w,h)
leer=led.frame(w,h)
anderes=led.frame(w,h)
x=-1
y=-1
a = 600
output=led.output()
map(lambda l: l.setColor(a,0,0), leer.getAllPixel())
map(lambda l: l.setColor(0,a,0), tmp.getAllPixel())
map(lambda l: l.setColor(0,0,a), anderes.getAllPixel())
t=0

while True:
	output.write(leer)
	time.sleep(0.02)
	output.write(tmp)
	time.sleep(0.02)
	output.write(anderes)
	time.sleep(0.02)

while True:
	x=0
	y=0
	color = (512 if bool(t % 2) else 0)
	if t>2:
		t=0
	for row in tmp.rows:
		y+=1
		for pt in row.leds:
			x+=1
			pt.setColor(color,color,color)
	
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	time.sleep(1/7)
	t+=1
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())
