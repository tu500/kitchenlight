import time
import math
from random import random

##Created by PiMa && Titan21


class movpix:
	def __init__(self,frame,targetX,targetY,color):
		self.frame = frame
		self.targetX = targetX
		self.targetY = targetY
		self.color = color
		self.currentX = 0
		self.currentY = -1
		self.oldColor = None

	def nextStep(self, t):
		if self.targetX == self.currentX and self.currentY == self.targetY:
			self.frame.getPixel(self.currentX, self.currentY).setColor(*self.getColor(t))
			return True

		if self.oldColor:
			self.frame.getPixel(self.currentX, self.currentY).setColor(*self.oldColor)

		if (self.currentY % 2) == 0:
			if self.currentX < self.frame.x - 1:
				self.currentX += 1
			else:
				self.currentY += 1
		else:
			if self.currentX > 0:
				self.currentX -= 1
			else:
				self.currentY += 1

		self.oldColor = self.frame.getPixel(self.currentX, self.currentY).getColor()		
		self.frame.getPixel(self.currentX, self.currentY).setColor(*self.getColor(t))

	def getColor(self, t):
		effectColor = self.mulitplyPlasma(self.currentX, self.currentY, t)		
		newColor = (effectColor[0] * self.color[0] / 1023,
			effectColor[1] * self.color[1] / 1023,
			effectColor[2] * self.color[2] / 1023) 
		return newColor

	def mulitplyPlasma(self, x, y, t):
		r = int(511+511*(math.sin((-0.2*x + 0.2*y + t+math.pi)) / 1))
		g = int(511+511*(math.sin((-0.2*x + 0.2*y + t+0.33*math.pi)) / 1))
		b = int(511+511*(math.sin((-0.2*x + 0.2*y + t+0.66*math.pi)) / 1))
		return ( r, g, b )

class pixelPic:
	def __init__(self, picture, frame, interval = 1.0):
		self.picture = picture
		self.frame = frame
		self.interval = interval
		self.reset()

	def loop(self):
		t = int((time.time() - self.startTime)/self.interval)
		while len(self.pixelList) < t - 1:
			if len(self.pixelList) >= (self.frame.x * self.frame.y) - 1:
				break
			x,y = self.getCoordsFromIndex(len(self.pixelList))
			self.pixelList.append(movpix(self.frame,x,y,self.picture[x][y]))

		done = False

		for p in self.pixelList:
			if p.nextStep(time.time()):
				done = True

		return done and len(self.pixelList) >= (self.frame.x * self.frame.y) - 1

	def reset(self):
		self.pixelList = []
		self.startTime = time.time()

	def getCoordsFromIndex(self, index):
		i = (self.frame.x * self.frame.y) - index - 1
		y = int(math.floor(i/self.frame.x))
		if y % 2 == 0:
			x = i % self.frame.x
		else:
			x = self.frame.x - ( i % self.frame.x) - 1
		return (x,y)	

class controller:
	def __init__(self, picList):
		self.picList = picList
		self.iterator = iter(picList)
		self.setPicture(self.iterator.next())

	def loop(self):
		if self.currentPicture.loop():
			try:
				self.setPicture(self.iterator.next())
			except StopIteration:
				self.iterator = iter(self.picList)
				self.setPicture(self.iterator.next())

	def setPicture(self, pic):
		self.currentPicture = pic
		pic.reset()
