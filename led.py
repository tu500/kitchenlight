import sys
import time
import parport
import PIL

import random

class szene:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frames = []

    def testColors(self, r=1, g=1, b=1):
        tmp = frame(self.x, self.y)
        output = parport()
        map(lambda l: l.setColor(r,g,b), tmp.getAllPixel())
        #self.frames.append( tmp )
        output.write(tmp)

    def flushAll(self):
        tmp = frame(self.x, self.y)
        output = parport()
        map(lambda l: l.setColor(0,0,0), tmp.getAllPixel())
        #self.frames.append( tmp )
        output.write(tmp)


class output:
    def __init__(self):
        #self.port = parport.Parport()
        parport.open();
        self.enable = 0
        self.latch = 0

    def write(self, frame):
        self.enable=0
        self.latch=0
        out = frame.toSerialOneLine()
        preparedData = 0
        preparedData=preparedData|(self.enable<<5)
        preparedData=preparedData|(self.latch<<4)
        #now = time.time()
        for element in out:
            for i in xrange(31,-1,-1):
                data=preparedData
                data=data|(((element>>i)&1)<<6)
                parport.writeWithClock(data)
                #time.sleep(0.000000000000005)
                #data=data|(1<<3)
                #parport.write(data)
                #time.sleep(0.0000000005)
        #print time.time()-now
        self.latch=1
        self.enable=0
        data=0
        data=data|(self.enable<<5)
        data=data|(self.latch<<4)
        parport.write(data)
        #time.sleep(0.000000015)
        self.enable=1
        self.latch=0
        data=0
        data=data|(self.enable<<5)
        data=data|(self.latch<<4)
        parport.write(data)
        #time.sleep(0.0000000015)
    
    
class frame:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rows = map( row, range(y), [x]*y )

    def copy(self):
        t = frame(self.x, self.y)
        for x in range(self.x):
            for y in range(self.y):
                t.getPixel(x,y).setColor(*self.getPixel(x,y).getColor())
        return t

    def toSerial(self):
        out = map(lambda r: r.toSerial(), self.rows)
        return out

    def toSerialOneLine(self):
        out = map(lambda r, pos: r.toSerial( (pos+1)%2 ), self.rows, range(len(self.rows)))
        out = reduce(lambda first,second: first+second, out)
        out.reverse()
        return out

    def getPixel(self, x, y):
        return self.rows[y].getPixel(x)

    def getAllPixel(self):
        return reduce(lambda first,second: first+second, map(lambda row: row.getAllPixel(), self.rows))

    def fillColor(self, color):
        for row in self.rows:
            for pt in row.leds:
                pt.setColor(*color)

    def fillRandom(self, colors):
        for row in self.rows:
            for pt in row.leds:
                pt.setColor(*colors[random.randint(0,len(colors)-1)])

    def flood(self, color, x=0, y=0):
        curColor = self.getPixel(x,y).getColor()
        if curColor == color:
            return
        self._floodRecursive(color, curColor, x, y)

    def _floodRecursive(self, color, curColor, x, y):
        if curColor != self.getPixel(x,y).getColor():
            return

        self.getPixel(x,y).setColor(*color)
        if x > 0: self._floodRecursive(color, curColor, x - 1, y)
        if y > 0: self._floodRecursive(color, curColor, x, y - 1)
        if x < self.x - 1: self._floodRecursive(color, curColor, x + 1, y)
        if y < self.y - 1: self._floodRecursive(color, curColor, x, y + 1)
         
class row:
    def __init__(self, rownumber, size):
        self.rownumber = rownumber
        self.leds = map( led, [0]*size )

    def _toSerial(self):
        return map(lambda point: point.toSerial(), self.leds)
    def toSerial(self, reverse=0):
        out = self._toSerial()
        if reverse == 0:
            out.reverse()
        return out 

    def getPixel(self, x):
        return self.leds[x]
    def getAllPixel(self):
        return self.leds
    


class led:
    def __init__(self, red=0, green=0, blue=0):
        self._red = 0
        self._green = 0
        self._blue = 0
        self.setColor(red, green, blue)

    def _setRed(self, r):
        #print r
        if r < 0 or r > 0b1111111111:
            raise Exception("Out of color range")
        self._red = r
    def _getRed(self):
        return self._red
    red = property(_getRed, _setRed)

    def _setGreen(self, green):
        if green < 0 or green > 0b1111111111:
            raise Exception("Out of color range")
        self._green = green
    def _getGreen(self):
        return self._green
    green = property(_getGreen, _setGreen)

    def _setBlue(self, blue):
        if blue < 0 or blue > 0b1111111111:
            raise Exception("Out of color range")
        self._blue = blue
    def _getBlue(self):
        return self._blue
    blue = property(_getBlue, _setBlue)

    def setColor(self, r, g, b):
        self._setRed(r)
        self._setGreen(g)
        self._setBlue(b)

    def getColor(self):
        return (self.red, self.green, self.blue)

    def toSerial(self):
        #print self._red
        out = 0
        out=(self._green<<0)|(self._red<<10)|(self._blue<<20)   
        return out
