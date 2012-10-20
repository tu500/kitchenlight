import led
import time
import math
import kitchen

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"



w=30
h=6

class Flash(kitchen.App):
    name = "Flash"
    description = "Flashes"
    interval = 0.02
    
    def __init__(self):
        kitchen.App.__init__(self)
        
    def onStart(self):
        a = 600
        self.output=led.output()
        self.frames = [led.frame(w,h) for i in range(3)]
        self.frames[0].fillColor((a,0,0))
        self.frames[1].fillColor((0,a,0))
        self.frames[2].fillColor((0,0,a))
        self.index = 0
    
    def update(self, passedtime):
        self.output.write(self.frames[self.index])
        self.index += 1
        self.index %= 3
