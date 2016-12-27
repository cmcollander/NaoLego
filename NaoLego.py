#! /usr/bin/python

# TODO: Write functions sendBlockList, waitForNoMotion, verifyBlocks
# TODO: Have the Nao relay the webserver information to the user to ensure they have the display
# TODO: Obtain data such as time to add block, number of incorrect blocks, and individual error counters for wrong coordinates, wrong color, wrong size, etc.
# TODO: At the end of the program, save the obtained data to a CSV file for future processing.
# TODO: Create a starting dialog for Nao to tell the user how the assembly program works

from LegoBlock import LegoBlock
from naoqi import ALProxy
import SimpleHTTPServer
import SocketServer
import os
from shutil import copyfile

SERVERPORT = 8080 # What port number with the hosted webserver be run on?
NUMBLOCKS = 5 # Represents the number of blocks we will assemble
IP = "127.0.0.1" # IP Address of the Nao. Since this is run from the Nao, this is localhost
tts = ALProxy("ALTextToSpeech",IP,9559) # Handles speech from the Nao

blockList = [] # Reperesents a list of LegoBlocks. Is initialized as empty

# Starts a webserver to display index.html. Is run in a separate thread
def webServerThread():
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = socketServer.TCPServer((",SERVERPORT),Handler)
	httpd.serve_forever()

# Decides a new lego block to add to the blockList. Randomly determined, no parameters or returns. Modifies blockList
# Places a new block at a new layer on top of all previous blocks. Ensure the block does connect through at least
# one lego peg to the layer beneath it.
# If the new block's x coord is less than 0, shift all blocks to the right until the block's x coord is 0.
# The first layer is y coord 0, second is y coord 1, etc. Keep in mind that a 'standard' block is a height of 2 layers
def addBlock():
	# Find the current layer
	layer = 0
	for block in blockList:
		layer += block.getHeight() # Increase Layer by the height of the block
	height = random.choice([1,2]) # The height can be either 1 or 2
	width = random.randrange(1,5) # The width can be between 1 and 4

	if layer==0:
		x = 0 # Our first block is placed at the origin
		y = 0 # Our first block is placed at the origin
	else: # If this is not our first block...
		below = blockList[-1] # Obtain the block on the below layer, which should be the last placed in the list
		left = below.x-(width-1) # Obtain our leftmost possible location
		right = below.width+below.x - 1 # Obtain our rightmost possible location
		x = random.randrange(left,right+1) # The X coordinate is determined from Left and Right
		y = layer # The Y coordinate is the current layer
	color = random.choice(["BLUE","RED","GREEN","YELLOW"]) # Find our color from these selections
	newBlock = LegoBlock(width,height,color,x,y) # Create our new block from the generated information
	blockList.append(newBlock) # Place our new block into our blockList
	# Shift all blocks to the right so they are all nonnegative coordinates
	v = []
	for block in blockList:
		v.append(block.x)
	offset = -1*min(v) # Determine the offset by the negative of the most leftmost x coordinate
	for block in blockList:
		block.x = block.x + offset

# TODO: Write this function
# Creates an image of the blockList and sends it out to a web server
# No returns, No parameters, No variable modifications, Modifies the image file for the web server (image.jpg)
def sendBlockList():
	pass

# Sends a default image for the introduction to the web server
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
# Just need to remove image.jpg and copy resources/init_screen.jpg to image.jpg.
def sendInitScreen():
	os.remove('image.jpg')
	copyfile('resources/init_screen.jpg','image.jpg')

# Sends an image for the finished program to the web server
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
# Just need to remove image.jpg and copy resources/fin_screen.jpg to image.jpg.
def sendFinScreen():
	os.remove('image.jpg')
	copyfile('resources/fin_screen.jpg','image.jpg')

# Tells the NAO to say a message. Takes the message as a string parameters. No returns or modifications
def NaoSay(s):
	tts.say(s)

# TODO: Write this function
# This function continuously runs until there is 2 seconds of no motion on the camera. At this point, we may have the blocks on the board
# Need to keep into account a blank board and the initial blockList before the user removes the blocks from the board
# Returns nothing, Modifies nothing, No parameters
# POSSIBLE IMPLEMENTATION: Obtain two sequential video frames and determine their absdiff(frame1,frame2). Obtain the average value and if
# it is below a specified threshold, then there is no motion. Start a timer for 2 seconds whenever motion is determined and if this timer
# ever reaches it's goal, we are good to leave the function.
def waitForNoMotion():
	pass

# TODO: Write this function
# This function verifies that the blocks on the board match the blockList. Returns either True or False, with True being a match
# No parameters, No modifications
def verifyBlocks():
	pass

# -------------- MAIN -------------------------

# First thing, start our webserver
thread.start_new_thread(webServerThread,())	
			
NaoSay("Hello! Thank you for playing my Lego Assembly game.")

# First block
addBlock()
NaoSay("Lets start by adding a single block")
sendBlockList()
waitForNoMotion()
while not verifyBlocks:
	NaoSay("I'm sorry, that is not the correct block. Please place the block shown in the image.")
	waitForNoMotion()

# Ready for additional blocks
for lcv in range(NUMBlOCKS-1): # -1 since we already placed 1 block
	addBlock()
	NaoSay("Good Job. Now, please add this new block to the assembly.")
	waitForNoMotion()
	while not verifyBlocks:
		NaoSay("I'm sorry, that is not the correct block. Please place the block shown in the image.")
		waitForNoMotion()

NaoSay("Great job! I hope you enjoyed this exercise! Come play again soon!")
