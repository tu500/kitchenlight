import led
import time
import math
#from random import random
import random
from array import *
import multiprocessing
import curses
import kitchen

try:
    import psyco
    psyco.full()
except ImportError:
    print "psyco not avaible"



w=30
h=6

colorFrame=led.frame(w,h)
output=led.output()


#while True:
#   controller.loop()
#   output.write(tmp)
#   #time.sleep(0.005)


class Floodit(kitchen.App):
    actions = [
            ('0', { 'action': '0' }),
            ('1', { 'action': '1' }),
            ('2', { 'action': '2' }),
            ('3', { 'action': '3' }),
            ('4', { 'action': '4' }),
            ('5', { 'action': '5' }),
            ('6', { 'action': '6' }),
            ('7', { 'action': '7' }),
            ('8', { 'action': '8' }),
            ('9', { 'action': '9' }),
            ]

    colors = [ (100, 0, 0),
            (0, 100, 0),
            (0, 0, 100),
            (200, 200, 0),
            (200, 0, 200),
            (100, 100, 100)]

    def onStart(self):
        self.colorFrame = led.frame(w,h)
        self.colorFrame.fillRandom(self.colors)
        self.currentPos = (0,0)
        self.currentColor = self.colors[0]
        self.cursorColor = (1000,1000,1000)
        output.write(self.colorFrame)

    def event(self, e):
        try: i = int(e)
        except ValueError: return
        self.colorFrame.flood(self.colors[i])
        screen.addstr(0,0,'setcolor' + str(i))
        output.write(self.colorFrame)

screen = None
def main(scr):
    global screen
    screen = scr
    c = kitchen.Manager(scr, Floodit, [Floodit])
    c.run()

curses.wrapper(main)
