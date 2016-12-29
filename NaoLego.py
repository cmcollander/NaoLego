#! /usr/bin/python

# TODO: Write functions sendBlockList, waitForHeadTouch, verifyBlocks
# TODO: Pull blocks for AddBlock from a list of blocks that we actually have
# TODO: Obtain data such as time to add block, number of incorrect blocks, and individual error counters for wrong coordinates, wrong color, wrong size, etc.
# TODO: At the end of the program, save the obtained data to a CSV file for future processing.

from LegoBlock import LegoBlock
from naoqi import ALProxy
import SimpleHTTPServer
import SocketServer
import os
from shutil import copyfile
import time
import thread
import random
import numpy as np
import cv2
import copy

SERVERPORT = 8080 # What port number with the hosted webserver be run on?
NUMBLOCKS = 5 # Represents the number of blocks we will assemble
IP = "127.0.0.1" # IP Address of the Nao. Since this is run from the Nao, this is localhost
tts = ALProxy("ALTextToSpeech",IP,9559) # Handles speech from the Nao
motion = ALProxy("ALMotion","127.0.0.1",9559) # Handles joint movements for the Nao
posture = ALProxy("ALRobotPosture","127.0.0.1",9559) # Handles postures of the robot
camera = ALProxy("ALPhotoCapture","127.0.0.1",9559) # Handles the camera of the robot
Finished = False
perspective_mat = None # Holds the transformation matrix for the visual perspective
HEADANGLE = 0.28 # Calibrated so he does not see his feet

# What lego blocks do we have?
presentBlockList = [] # Represents the list of LegoBlocks we actually have
red4x1 = LegoBlock(4,1,(0,0,255),0,0)
green4x1 = LegoBlock(4,1,(0,255,0),0,0)
blue4x1 = LegoBlock(4,1,(255,0,0),0,0)
red2x1 = LegoBlock(2,1,(0,0,255),0,0)
green2x1 = LegoBlock(2,1,(0,255,0),0,0)
blue2x1 = LegoBlock(2,1,(255,0,0),0,0)
presentBlockList.append(red4x1)
presentBlockList.append(green4x1)
presentBlockList.extend(4*[copy.deepcopy(blue4x1)])
presentBlockList.extend(3*[copy.deepcopy(red2x1)])
presentBlockList.extend(3*[copy.deepcopy(green2x1)])
presentBlockList.extend(2*[copy.deepcopy(blue2x1)])
random.shuffle(presentBlockList) # Shuffle our presentBlockList

blockList = [] # Represents a list of LegoBlocks. Is initialized as empty

# Initializes the camera settings
def initCamera():
	camera.setResolution(2)
	camera.setPictureFormat("jpg")
	camera.setCameraID(1)

# Starts a webserver to display index.html. Is run in a separate thread
def webServerThread():
	SocketServer.TCPServer.allow_reuse_address = True
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("",SERVERPORT),Handler)
	while not Finished:
		httpd.handle_request()
	httpd.shutdown()
	httpd.server_close()

# Decides a new lego block to add to the blockList. Randomly determined from list of available blocks, no parameters or returns. Modifies blockList
# Places a new block at a new layer on top of all previous blocks. Ensure the block does connect through at least one lego peg to the layer beneath it.
# If the new block's x coord is less than 0, shift all blocks to the right until the block's x coord is 0.
# The first layer is y coord 0, second is y coord 1, etc. Keep in mind that a 'standard' block is a height of 2 layers
def addBlock():
	# Find the current layer
	layer = 0
	for block in blockList:
		layer += block.getHeight() # Increase Layer by the height of the block
	newBlock = presentBlockList.pop() # Get a new block from our presentBlockList
	height = newBlock.getHeight()
	width = newBlock.getWidth()

	if layer==0:
		newBlock.setCoords(0,0) # Our first block is placed at the origin
	else: # If this is not our first block...
		below = blockList[-1] # Obtain the block on the below layer, which should be the last placed in the list
		left = below.x-(width-1) # Obtain our leftmost possible location
		right = below.width+below.x - 1 # Obtain our rightmost possible location
		newBlock.setCoords(random.randrange(left,right+1),layer) # The X coordinate is determined from Left and Right, The Y coordinate is the current layer
	blockList.append(newBlock) # Place our new block into our blockList
	
	# Find the block in the layer beneath and set any connected connectors to 1
	if len(blockList)>=2:
		thisBlockXList = range(newBlock.x,newBlock.x+newBlock.width)
		prevBlock = blockList[-2]
		prevBlockXList = range(prevBlock.x,prevBlock.x+prevBlock.width)
		inter = list(set(thisBlockXList)&set(prevBlockXList))
		subVal = inter[0]
		inter[:] = [x - subVal for x in inter]
		prevBlock.setBits(inter)
	
	# Shift all blocks to the right so they are all nonnegative coordinates
	v = []
	for block in blockList:
		v.append(block.x)
	offset = -1*min(v) # Determine the offset by the negative of the most leftmost x coordinate
	for block in blockList:
		block.x = block.x + offset

# TODO: Improve this function with nubs indicating connectors
# TODO: After image creation, add to a 640x480 image without distorting image for easier web display
# Creates an image of the blockList and sends it out to a web server
# No returns, No parameters, No variable modifications, Modifies the image file for the web server (image.jpg)
def sendBlockList():
	img = np.zeros((5,16,3), np.uint8)
	for x in range(16):
		for y in range(5):
			img[y,x] = (255,255,255)
	for block in blockList:
		y = block.y
		for x in range(block.x,block.x+block.width):
			img[y,x] = block.color
	res = cv2.resize(img, None, fx=60, fy=60, interpolation=cv2.INTER_NEAREST)
	res = cv2.flip(res,0)
	cv2.imwrite('image.jpg', res)

# Sends a default image for the introduction of the application
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
# Just need to remove image.jpg and copy resources/init_screen.jpg to image.jpg.
def sendInitScreen():
	if os.path.isfile('image.jpg'):
		os.remove('image.jpg')
	copyfile('resources/init_screen.jpg','image.jpg')

# Sends an image for the finished program to the web server
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
# Just need to remove image.jpg and copy resources/fin_screen.jpg to image.jpg.
def sendFinScreen():
	if os.path.isfile('image.jpg'):
		os.remove('image.jpg')
	copyfile('resources/fin_screen.jpg','image.jpg')

# Tells the NAO to say a message. Takes the message as a string parameters. No returns or modifications
def NaoSay(s):
	motion.setAngles("HeadPitch",0,0.1) # Look at the user
	tts.say(s) # Say our message
	motion.setAngles("HeadPitch",HEADANGLE,0.1) # Return to board

# TODO: Write this function
# The nao will prompt the user and wait until his head receives contact
def waitForHeadTouch():
	tts.say("Please touch my head when you are ready.")
	time.sleep(5)

# Ensure that for our perspective we have a consistent ordering of points
# http://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
def order_points(pts):
	rect = np.zeros((4,2),dtype="float32")
	s=pts.sum(axis=1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	diff = np.diff(pts,axis=1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	return rect
			
# Obtain an image of the blank paper and determine our critical points and our perspective matrix
def initPerspective():
	global perspective_mat
	pic = camera.takePicture("/home/nao/NaoLego/","frame")
	img = cv2.imread(pic[0])
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(gray,4,0.01,10)
	corners = np.float32([corners[0][0],corners[1][0],corners[2][0],corners[3][0]])
	perspective_pts = order_points(corners)
	dst = np.array([
		[0, 0],
		[639, 0],
		[639, 479],
		[0, 479]], dtype = "float32")
	perspective_mat = cv2.getPerspectiveTransform(perspective_pts,dst)
	# Create an image of our initial image overlayed with our perspective points
	p_img = img
	p_list = perspective_pts.tolist()
	cv2.circle(p_img,(int(p_list[0][0]),int(p_list[0][1])),10,(255,0,0),-1)
	cv2.circle(p_img,(int(p_list[1][0]),int(p_list[1][1])),10,(0,255,0),-1)
	cv2.circle(p_img,(int(p_list[2][0]),int(p_list[2][1])),10,(0,0,255),-1)
	cv2.circle(p_img,(int(p_list[3][0]),int(p_list[3][1])),10,(0,0,0),-1)
	cv2.imwrite("perspective.jpg",p_img)
	
			
# Apply perspective correction
def perspectiveCorrection(frame):
	return cv2.warpPerspective(frame,perspective_mat,(640,480))
			
# TODO: Write this function
# This function verifies that the blocks on the board match the blockList. Returns either True or False, with True being a match
# No parameters, No modifications
def verifyBlocks():
	pic = camera.takePicture("/home/nao/NaoLego/","frame")
	img = perspectiveCorrection(cv2.imread(pic[0])) # Apply perspective correction to our image
	cv2.imwrite("frameP.jpg",img) # Save our new perspectivized image to frameP.jpg
	# TODO: Analyze image here
	return True

# -------------- MAIN -------------------------

# First thing, start our webserver
sendInitScreen()
thread.start_new_thread(webServerThread,())

# Prepare our camera
initCamera()

# Get the NAO in the correct position
posture.goToPosture("StandInit",1.0)
			
NaoSay("Hello! Thank you for playing my Lego Assembly game. First, please ensure that the board in front of me is clear and you have logged into my webserver. My server address is 192.168.1.12 port 8 0 8 0.")
waitForHeadTouch()

# Determine the points of our paper and our perspective
motion.setAngles("HeadPitch",HEADANGLE,0.1)
time.sleep(1) # Allow time for our head to reach the correct location before obtaining points
initPerspective()

# First block
addBlock()
NaoSay("Lets start by adding a single block")
sendBlockList()
waitForHeadTouch()
while not verifyBlocks():
	NaoSay("I'm sorry, that is not the correct block. Please place the block shown in the image.")
	waitForHeadTouch()

# Ready for additional blocks
for lcv in range(NUMBLOCKS-1): # -1 since we already placed 1 block
	addBlock()
	sendBlockList()
	NaoSay("Good Job. Now, please add this new block to the assembly.")
	waitForHeadTouch()
	while not verifyBlocks():
		NaoSay("I'm sorry, that is not the correct block. Please place the block shown in the image.")
		waitForHeadTouch()

sendFinScreen()
Finished = True
NaoSay("Great job! I hope you enjoyed this exercise! Come play again soon!")
