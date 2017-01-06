# LegoBlock represents a single lego block which has the following properties
# * Width  - How many horizontal lego connectors does the block have?
# * Height - How vertically thick is the lego block? The thin block represents 1, while the 'normal' sized block represents 2
# * Color  - What color is the lego block, saved as a full capital string
# * Coords - What is the coordinate of the bottom left of the block according to the coordinate system in the diagram

class LegoBlock:
	def __init__(self,w,h,col,x,y):
		self.width = w
		self.height = h
		self.color = col # Color is currently a string. May change to RGB value or MatPlotLib Color object in the future
		self.coords = (x,y) # Coordinates are stored as a tuple
		self.x = x
		self.y = y
		self.bitArray = [False]*w  # Represents if a block's connectors are connected to the layer above. Inits as all unconnected

	def setBits(self,bits):
		for bit in bits:
			self.bitArray[bit] = True
			
	def getbitArray(self):
		return self.bitArray
	
	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getCoords(self):
		return self.coords

	def getColor(self):
		return self.color

	def setWidth(self,w):
		self.width = w

	def setHeight(self,h):
		self.height = h

	def setCoords(self,x,y):
		self.coords = (x,y)
		self.x = x
		self.y = y

	def setColor(self,c):
		self.color = c


