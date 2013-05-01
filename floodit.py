import led
import time
import random
from array import *
import kitchen

try:
    import psyco
    psyco.full()
except ImportError:
    print "psyco not avaible"

w=30
h=6

class Floodit(kitchen.App):
    name = "Floodit"
    description = "The floodit game"

    colors = {
            'red':    ('r', (100, 0, 0)),
            'green':  ('g', (0, 100, 0)),
            'blue':   ('b', (0, 0, 100)),
            'yellow': ('y', (200, 200, 0)),
            'purple': ('p', (200, 0, 200)),
            'white':  ('w', (100, 100, 100)),
        }

    def onStart(self):
        self.setActionsAndKeymap()
        self.output = led.output()
        self.colorFrame = led.frame(w,h)
        self.colorFrame.fillRandom(map(lambda x: x[1], self.colors.itervalues()))
        self.output.write(self.colorFrame)

    def setActionsAndKeymap(self):
        self.actions = []
        for name, (key, rgb) in self.colors.iteritems():
            self.keyToEvent[ord(key)] = name
            self.actions.append((name, { 'action': name }, {}, rgb))

    def event(self, e, args={}):
        try:
            self.colorFrame.flood(self.colors[e][1])
            self.output.write(self.colorFrame)
        except KeyError:
            return
