import led
import kitchen

try:
        import psyco
        psyco.full()
except ImportError:
        print "psyco not avaible"

w=30
h=6

class Empty(kitchen.App):
    name = "Empty"
    description = "Draws... nothing"

    def onStart(self):
        led.output().write(led.frame(w,h))
