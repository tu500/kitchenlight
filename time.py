import led
import time
import math
import Image
import ImageSequence,ImageFont,ImageDraw
from time import gmtime, strftime, localtime

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"



w=30
h=6

tmp = led.frame(w,h)
leer=led.frame(w,h)
x=-1
y=-1

font = ImageFont.truetype("pixelmix.ttf", 6)
text = "Time:"
print strftime("%H%M%S", localtime())
size = font.getsize(text)

if size[0] > w:
	scrolling = True
	text_width = size[0]
else:
	text_width = w

output=led.output()

offset = 0
while True:
	text = strftime("%H%M%S", localtime())
	image = Image.new("RGB",(text_width,h),(0,0,0))
	draw = ImageDraw.Draw(image)
	draw.fontmode = "1"
	draw.text((0,0), text, fill=(1,1,10), font=font)
	data = image.load()


	offset = offset % 30
	for (x,y) in reduce(lambda x,z: x+z, map(lambda y: map(lambda x: (x,y), range(30)), range(6))):
		pt = tmp.getPixel(((x+offset)%30),y)
		color=data[x%text_width,y]
		pt.setColor(color[0]<<2,color[1]<<2,color[2]<<2)
			
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	time.sleep(0.05)
	#offset -= 1

