import led
import kitchen
from random import random

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"

w=30
h=6

class Randompic(kitchen.App):
    name = "Randompic"
    description = "Testanimation"
    interval = 0.05

    maxcol = 1023

    def onStart(self):
        self.output = led.output()
        self.frame = led.frame(w,h)

    def update(self, passedtime):
        for row in self.frame.rows:
            for pt in row.leds:
                r = 0
                b = 0
                g = 0
                while(r + g + b < 1):
                    if(  (int(random()*1000)) % 3 == 0):
                        r = int(self.maxcol)
                    elif((int(random()*1000)) % 3 == 1):
                        g = int(self.maxcol)
                    elif((int(random()*1000)) % 3 == 2):
                        b = int(self.maxcol)
                pt.setColor(r,g,b)
        self.output.write(self.frame)
