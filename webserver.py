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

from empty   import Empty
from test    import Test
from randompic import Randompic
from floodit import Floodit
from text import Text
from timeDisplay import TimeDisplay
from moodlight import Moodlight
from flash import Flash
from runpoints import Runpoints

screen = None
def main(scr):
    global screen
    screen = scr
    apps = [
        Empty,
        Floodit,
        Text,
        TimeDisplay,
        Test,
        Runpoints,
        Randompic,
        Flash,
        Moodlight]
    c = kitchen.Manager(scr, Empty, apps)
    c.run()

curses.wrapper(main)
