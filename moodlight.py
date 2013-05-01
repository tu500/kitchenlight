import led
import time
import math
#from random import random
import random
from array import *
import multiprocessing
import curses
import kitchen

def clamp(i, a, b):
    if i < a: return a
    if i > b: return b
    return i

try:
    import psyco
    psyco.full()
except ImportError:
    print "psyco not avaible"

w=30
h=6

class Moodlight(kitchen.App):
    name = "Moodlight"
    description = ""
    maxcol = 1023
    change = 20

    actions = [
            ('set color',   { 'action': 'setcolor' }, [ ('r',4,4), ('g',4,4), ('b',4,4)]),
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

    def event(self, e, args={}):
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
        if e == 'setcolor':
            try: self.r = clamp(int(args['r']), 0, self.maxcol)
            except ValueError: pass
            try: self.g = clamp(int(args['g']), 0, self.maxcol)
            except ValueError: pass
            try: self.b = clamp(int(args['b']), 0, self.maxcol)
            except ValueError: pass
        self.updateColor()

    def updateColor(self):
        self.frame.fillColor((self.r, self.g, self.b))
        self.output.write(self.frame)

    def getInfo(self, request):
        return "Current Color: %d, %d, %d" % (self.r, self.g, self.b)
