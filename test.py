import led
import math
import kitchen

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"

w=30
h=6

class Test(kitchen.App):
    name = "Test"
    description = "Testanimation"
    interval = 0.05

    def onStart(self):
        self.output = led.output()
        self.frame = led.frame(w,h)

    def update(self, passedtime):
        x=0
        y=0
        t = self.runtime % 300
        for row in self.frame.rows:
            y+=1
            for pt in row.leds:
                x+=1
                r = int(511+511*(math.sin((0.02*x + 0.02*y + t)) / 1))
                g = int(511+511*(math.sin((0.02*x + 0.02*y + t+0.66*math.pi)) / 1))
                b = int(511+511*(math.sin((0.02*x + 0.02*y + t+1.33*math.pi)) / 1))
                pt.setColor(r,g,b)
        self.output.write(self.frame)
