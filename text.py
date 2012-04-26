import led
import time
import math
import Image,ImageSequence,ImageFont,ImageDraw

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

font = ImageFont.truetype("pixelmix.ttf", 6)
text = "i'm rollin, they hatin"
size = font.getsize(text)

if size[0] > w:
	scrolling = True
	text_width = size[0]
else:
	text_width = w

image = Image.new("RGB",(text_width,h),(0,0,0))
draw = ImageDraw.Draw(image)
draw.text((0,0), text, fill=(0,255,0), font=font)
#image.save("test.png")
data = image.load()

output=led.output()

offset = 0
while True:
	offset = offset % 30
	for (x,y) in reduce(lambda x,z: x+z, map(lambda y: map(lambda x: (x,y), range(30)), range(6))):
		pt = tmp.getPixel(((x+offset)%30),y)
		color=data[x%text_width,y]
		pt.setColor(color[0]<<2,color[1]<<2,color[2]<<2)
			
	#output.write(leer)
	#time.sleep(1)
	output.write(tmp)
	time.sleep(0.05)
	offset -= 1
#map(lambda l: l.setColor(5,0,0), tmp.getAllPixel())

