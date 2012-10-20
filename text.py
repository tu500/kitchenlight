import led
import time
import Image,ImageSequence,ImageFont,ImageDraw
import kitchen

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"



w=30
h=6


class Text(kitchen.App):
    name = "Text"
    description = "Prints arbitrary text"
    interval = 0.02

    def __init__(self, text="1234567890 The Quick brown Fox jumps over the lazy dog. -!\$%&/()=?"):
        kitchen.App.__init__(self)
        self.font = ImageFont.truetype("pixelmix.ttf", 6)
        self.setText(text)

    def onStart(self):
        self.output = led.output()
        self.frame = led.frame(w,h)

    def setText(self, text):
        self.text = text
        size = self.font.getsize(text)

        if size[0] > w:
            self.scrolling = True
            self.text_width = size[0]
        else:
            self.text_width = w

        image = Image.new("RGB",(self.text_width,h),(0,0,0))
        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"
        draw.text((0,0), text, fill=(20,20,20), font=self.font)
        self.data = image.load()

        self.runtime = 0.0

    def update(self, passedtime):
        offset = int((self.runtime * 10) % self.text_width)
        for (x,y) in reduce(lambda x,z: x+z, map(lambda y: map(lambda x: (x,y), range(30)), range(6))):
            pt = self.frame.getPixel(x,y)
            color=self.data[(x+offset)%self.text_width,y]
            pt.setColor(color[0]<<2,color[1]<<2,color[2]<<2)

        self.output.write(self.frame)
