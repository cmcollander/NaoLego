#! /usr/bin/python

# TODO: Write functions addBlock, sendBlockList, sendInitScreen, sendFinScreen, waitForNoMotion, verifyBlocks
# TODO: Have the Nao relay the webserver information to the user to ensure they have the display
# TODO: Obtain data such as time to add block, number of incorrect blocks, and individual error counters for wrong coordinates, wrong color, wrong size, etc.
# TODO: A the end of the program, save the obtained data to a CSV file for future processing.
# TODO: Start an external webserver on the Nao that will load index.html through one of the Nao's ports.
# TODO: Create a starting dialog for Nao to tell the user how the assembly program works

from LegoBlock import LegoBlock
from naoqi import ALProxy

NUMBLOCKS = 5 # Represents the number of blocks we will assemble
IP = "127.0.0.1" # IP Address of the Nao. Since this is run from the Nao, this is localhost
tts = ALProxy("ALTextToSpeech",IP,9559) # Handles speech from the Nao

blockList = [] # Reperesents a list of LegoBlocks. Is initialized as empty

# TODO: Write this function 
# Decides a new lego block to add to the blockList. Randomly determined, no parameters or returns. Modifies blockList
# Places a new block at a new layer on top of all previous blocks. Ensure the block does connect through at least
# one lego peg to the layer beneath it.
# If the new block's x coord is less than 0, shift all blocks to the right until the block's x coord is 0.
# The first layer is y coord 0, second is y coord 1, etc. Keep in mind that a 'standard' block is a height of 2 layers
def addBlock():
	pass

# TODO: Write this function
# Creates an image of the blockList and sends it out to a web server
# No returns, No parameters, No variable modifications, Modifies the image file for the web server (image.jpg)
def sendBlockList():
	pass

# TODO: Write this function
# Sends a default image for the introduction to the web server
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
def sendInitScreen():
	pass

# TODO: Write this function
# Sends an image for the finished program to the web server
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
def sendFinScreen():
	pass

# Tells the NAO to say a message. Takes the message as a string parameters. No returns or modifications
def NaoSay(s):
	tts.say(s)

# TODO: Write this function
# This function continuously runs until there is 2 seconds of no motion on the camera. At this point, we may have the blocks on the board
# Need to keep into account a blank board and the initial blockList before the user removes the blocks from the board
# Returns nothing, Modifies nothing, No parameters
def waitForNoMotion():
	pass

# TODO: Write this function
# This function verifies that the blocks on the board match the blockList. Returns either True or False, with True being a match
# No parameters, No modifications
def verifyBlocks():
	pass

# -------------- MAIN -------------------------

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