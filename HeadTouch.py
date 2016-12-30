from naoqi import ALModule
from naoqi import ALProxy

HeadTouch = None
memory = None

class HeadTouch(ALModule):
	def __init__(self,name):
		ALModule.__init__(self,name)
		global memory
		memory = ALProxy("ALMemory")
		memory.subscribeToEvent("TouchChanged","HeadTouch","onTouched")

	def onTouched(self,strVarName,value):
		memory.unsubscribeToEvent("TouchChanged","HeadTouch")

		touched_bodies = []
		for p in value:
			if p[1]:
				touched_bodies.append(p[0])

		for body in touched_bodies:
			if body[:4]=='Head':
				self.touched = True

		memory.subscribeToEvent("TouchChanged","HeadTouch","onTouched")

	def isTouched(self):
		return self.touched

	def resetTouched(self):
		self.touched = False
