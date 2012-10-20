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


a = 200
colors = [ (a, 0, 0),
        (0, a, 0),
        (0, 0, a)]

w=30
h=6

colorFrame=led.frame(w,h)
leer=led.frame(w,h)

output=led.output()
interval = 0.2


#while True:
#   controller.loop()
#   output.write(tmp)
#   #time.sleep(0.005)



for row in colorFrame.rows:
    for pt in row.leds:
        pt.setColor(*colors[random.randint(0,len(colors)-1)])

def main(scr):
    scr.nodelay(1)
    scr.keypad(1)

    starttime = time.time()
    currentPos = (0,0)
    currentColor = colors[0]
    cursorColor = (1000,1000,1000)

    while True:
        c = scr.getch()
        if c == ord('q'): exit()
        elif c == ord('w'): currentPos = (currentPos[0], currentPos[1] - 1)
        elif c == ord('s'): currentPos = (currentPos[0], currentPos[1] + 1)
        elif c == ord('d'): currentPos = (currentPos[0] + 1, currentPos[1])
        elif c == ord('a'): currentPos = (currentPos[0] - 1, currentPos[1])
        elif c in range(ord('0'), ord('9')):
            currentColor = colors[c - ord('0')]
        elif c == 10:

        tmp = colorFrame.copy()
        timepassed = int(time.time() - starttime)
        if timepassed % 2 or True:
            tmp.getPixel(*currentPos).setColor(*cursorColor)
        output.write(tmp)
    
curses.wrapper(main)
