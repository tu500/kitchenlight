import led
import time
import math
#from random import random
import random
from array import *
import multiprocessing
import curses

try:
    import psyco
    psyco.full()
except ImportError:
    print "psyco not avaible"


# 2012-10-19 by Titan21

a = 204

w=30
h=6

colorFrame=led.frame(w,h)
leer=led.frame(w,h)

output=led.output()
maxcol = 600
change = 20
r = 200
g = 200
b = 200


def main(scr):
    global r,g,b
    scr.nodelay(1)
    scr.keypad(1)
    scr.addstr(0,0, repr("Interactive Moodlight.")) 
    scr.addstr(1,0, repr("r-t-z to increase r-g-b"))
    scr.addstr(2,0, repr("f-g-h to decrease"))
    scr.addstr(3,0, repr("v,b,n to nullify"))
    scr.addstr(4,0, repr("p to print color"))
    scr.addstr(6,0, repr("Achja; q to quit"))

    while True:
        c = scr.getch()
        if c == ord('q'): exit()
        elif c == ord('r') and r + change <= maxcol  : r += change
        elif c == ord('f') and r - change >= 0       : r -= change
        elif c == ord('t') and g + change <= maxcol  : g += change
        elif c == ord('g') and g - change >= 0       : g -= change
        elif c == ord('z') and b + change <= maxcol  : b += change
        elif c == ord('h') and b - change >= 0       : b -= change
        elif c == ord('v') : r = 0
        elif c == ord('b') : g = 0
        elif c == ord('n') : b = 0
        elif c == ord('p'): scr.addstr(9,0, repr((r,g,b)))
        colorFrame.fillColor((r,g,b))
        output.write(colorFrame)

curses.wrapper(main)

