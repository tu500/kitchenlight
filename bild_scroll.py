import led
import time
import math
import Image
import sys
import os
import fcntl

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"


if len(sys.argv) == 2:
	sl = float(sys.argv[1])
else:
	sl = 0.05

w=30
h=6

tmp=led.frame(w,h)
leer=led.frame(w,h)
x=-1
y=-1

output=led.output()
image=Image.open('bild.png')
data = image.load()
print image.size
fd = sys.stdin.fileno()
fl = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

allpixel = reduce(lambda x,z: x+z, map(lambda y: map(lambda x: (x,y), range(30)), range(6)))
offset = 0
while True:
	offset = offset % 30
        for (x,y) in allpixel:
		pt = tmp.getPixel(((x+offset)%30),y)
		color=data[x,y]
		pt.setColor(color[0]<<2,color[1]<<2,color[2]<<2)
			
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	time.sleep(sl)
	offset += 1
	try:
		sl = float(sys.stdin.read())
	except IOError:
		pass
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())
