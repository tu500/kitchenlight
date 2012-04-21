
class szene:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.frames = []

	def testRed(self):
		tmp = frame(self.x, self.y)
		map(lambda l: l.setColor(255,1,0), tmp.getAllPixel())
		#self.frames.append( tmp )
		return tmp



class frame:
	def __init__(self, x, y):
		self.x = x
		self.rows = map( row, range(y), [x]*y )

	def toSerial(self):
		out = map(lambda r: r.toSerial(), self.rows)
		return out
	def toSerialOneLine(self):
		out = map(lambda r, pos: r.toSerial( pos%2 ), self.rows, range(len(self.rows)))
		out = reduce(lambda first,second: first+second, out)
		return out

	def getPixel(self, x, y):
		return self.rows[y].getPixel(x)
		
	def getAllPixel(self):
		return reduce(lambda first,second: first+second, map(lambda row: row.getAllPixel(), self.rows))
		

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
		print r
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

	def toSerial(self):
		print self._red
		out = 0
		out = (out <<  2) |(self._red&1023) 
		out = (out << 10) | (self._green&1024)
		out = (out << 10) | (self._blue&1024)
		
		return out
