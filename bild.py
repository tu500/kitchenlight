import led
import time
import math
import Image,ImageSequence

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
image=Image.open('bild.gif')

offset = 0
while True:
	offset = offset % 30
	for frame in ImageSequence.Iterator(image): 
		data=frame.load()
		for (x,y) in reduce(lambda x,z: x+z, map(lambda y: map(lambda x: (x,y), range(30)), range(6))):
			pt = tmp.getPixel(((x+offset)%30),y)
			color=data[x,y]
			pt.setColor(color[0]<<2,color[1]<<2,color[2]<<2)
			
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	time.sleep(0.05)
	offset += 1
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())
