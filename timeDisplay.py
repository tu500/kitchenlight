import time
from time import gmtime, strftime, localtime
from text import Text

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"

w=30
h=6

class TimeDisplay(Text):
    name = "TimeDisplay"
    description = "localtime"

    def __init__(self):
        Text.__init__(self, "")
        self.updateTime()

    def update(self, passedtime):
        self.updateTime()
        Text.update(self, passedtime)

    def updateTime(self):
        self.setText(strftime("%H%M%S", localtime()))
