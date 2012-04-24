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
x=-1
y=-1

output=led.output()
map(lambda l: l.setColor(1023,1023,1023), leer.getAllPixel())
t=0

while True:
	x=0
	y=0
	if t>300:
		t=0
	for row in tmp.rows:
		y+=1
		for pt in row.leds:
			x+=1
			#color = int(128.0 + (128.0 * math.sin(math.sqrt((x - w / 2.0) * (x - w / 2.0) + (y - h / 2.0) * (y - h / 2.0)) / 8.0)));
			r = int(511+511*(math.sin((0.02*x + 0.02*y + t)) / 1))
			g = int(511+511*(math.sin((0.02*x + 0.02*y + t+0.66*math.pi)) / 1))
			b = int(511+511*(math.sin((0.02*x + 0.02*y + t+1.33*math.pi)) / 1))
			pt.setColor(r,g,b)
	
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	#time.sleep(0.05)
	t+=0.1
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())
