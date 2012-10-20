import led
import time
import math
from random import random
from array import *
import movingPixel
import kitchen
try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"



w=30
h=6

class Runpoints(kitchen.App):
    name = "RunPoints"
    description = "Running Points"
    interval = 0.02

    def __init__(self):
        kitchen.App.__init__(self)
        self.pixStartInterval = 1.0

    def onStart(self):
        self.output=led.output()
        self.frame = led.frame(w,h)
        a = 20
        r = a
        g = a
        b = a
        pic1 = movingPixel.pixelPic([[(r,0,0) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        pic2 = movingPixel.pixelPic([[(0,g,0) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        pic3 = movingPixel.pixelPic([[(0,0,b) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        pic4 = movingPixel.pixelPic([[(r,g,0) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        pic5 = movingPixel.pixelPic([[(0,g,b) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        pic6 = movingPixel.pixelPic([[(r,0,b) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        pic7 = movingPixel.pixelPic([[(r,g,b) for i in range(h)] for j in range(w)], self.frame, self.pixStartInterval)
        self.controller = movingPixel.controller([pic7, pic4, pic6, pic1, pic5, pic2, pic3])

    def update(self, passedtime):
        self.controller.loop()
        self.output.write(self.frame)
