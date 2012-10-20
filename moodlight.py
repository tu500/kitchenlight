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

## 2012-10-19 by Titan21
#
#a = 204
#
#colorFrame=led.frame(w,h)
#leer=led.frame(w,h)
#
#output=led.output()
#maxcol = 600
#change = 20
#r = 200
#g = 200
#b = 200
#
#
#def main(scr):
#    global r,g,b
#    scr.nodelay(1)
#    scr.keypad(1)
#    scr.addstr(0,0, repr("Interactive Moodlight.")) 
#    scr.addstr(1,0, repr("r-t-z to increase r-g-b"))
#    scr.addstr(2,0, repr("f-g-h to decrease"))
#    scr.addstr(3,0, repr("v,b,n to nullify"))
#    scr.addstr(4,0, repr("p to print color"))
#    scr.addstr(6,0, repr("Achja; q to quit"))
#
#    while True:
#        c = scr.getch()
#        if c == ord('q'): exit()
#        elif c == ord('r') and r + change <= maxcol  : r += change
#        elif c == ord('f') and r - change >= 0       : r -= change
#        elif c == ord('t') and g + change <= maxcol  : g += change
#        elif c == ord('g') and g - change >= 0       : g -= change
#        elif c == ord('z') and b + change <= maxcol  : b += change
#        elif c == ord('h') and b - change >= 0       : b -= change
#        elif c == ord('v') : r = 0
#        elif c == ord('b') : g = 0
#        elif c == ord('n') : b = 0
#        elif c == ord('p'): scr.addstr(9,0, repr((r,g,b)))
#        colorFrame.fillColor((r,g,b))
#        output.write(colorFrame)
#
#curses.wrapper(main)


class Moodlight(kitchen.App):
    name = "Moodlight"
    description = ""
    maxcol = 1023
    change = 20

    actions = [
            ('red++',   { 'action': 'r+' }),
            ('red--',   { 'action': 'r-' }),
            ('red0',    { 'action': 'r0' }),
            ('green++', { 'action': 'g+' }),
            ('green--', { 'action': 'g-' }),
            ('green0',  { 'action': 'g0' }),
            ('blue++',  { 'action': 'b+' }),
            ('blue--',  { 'action': 'b-' }),
            ('blue0',   { 'action': 'b0' }),
        ]

    keyToEvent = {
            ord('r'): 'r+',
            ord('f'): 'r-',
            ord('v'): 'r0',
            ord('t'): 'g+',
            ord('g'): 'g-',
            ord('b'): 'g0',
            ord('z'): 'b+',
            ord('h'): 'b-',
            ord('n'): 'b0',
            ord('p'): 'print',
        }

    def onStart(self):
        self.output = led.output()
        self.frame = led.frame(w,h)
        self.r, self.g, self.b = 200, 200, 200
        self.updateColor()
        self.output.write(self.frame)

    def event(self, e):
        if e == 'r+' and self.r + self.change <= self.maxcol  : self.r += self.change
        if e == 'r-' and self.r - self.change >= 0            : self.r -= self.change
        if e == 'g+' and self.g + self.change <= self.maxcol  : self.g += self.change
        if e == 'g-' and self.g - self.change >= 0            : self.g -= self.change
        if e == 'b+' and self.b + self.change <= self.maxcol  : self.b += self.change
        if e == 'b-' and self.b - self.change >= 0            : self.b -= self.change
        if e == 'r0': self.r = 0
        if e == 'g0': self.g = 0
        if e == 'b0': self.b = 0
        if e == 'print': self.scr.addstr(0,0, repr((self.r,self.g,self.b)))
        self.updateColor()

    def updateColor(self):
        self.frame.fillColor((self.r, self.g, self.b))
        self.output.write(self.frame)
