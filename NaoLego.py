#! /usr/bin/python

# TODO: Write functions sendBlockList, waitForNoMotion, verifyBlocks
# TODO: Have the Nao relay the webserver information to the user to ensure they have the display
# TODO: Obtain data such as time to add block, number of incorrect blocks, and individual error counters for wrong coordinates, wrong color, wrong size, etc.
# TODO: At the end of the program, save the obtained data to a CSV file for future processing.
# TODO: Create a starting dialog for Nao to tell the user how the assembly program works
# TODO: Create a predefined posture named InitNaoLego for the NAO to start at (standing tall, looking down at calibration board)

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

SERVERPORT = 8080 # What port number with the hosted webserver be run on?
NUMBLOCKS = 5 # Represents the number of blocks we will assemble
IP = "127.0.0.1" # IP Address of the Nao. Since this is run from the Nao, this is localhost
tts = ALProxy("ALTextToSpeech",IP,9559) # Handles speech from the Nao
motion = ALProxy("ALMotion","127.0.0.1",9559) # Handles joint movements for the Nao
posture = ALProxy("ALRobotPosture","127.0.0.1",9559) # Handles postures of the robot
camera = ALProxy("ALPhotoCapture","127.0.0.1",9559) # Handles the camera of the robot
Finished = False
perspective_mat = None
HEADANGLE = 0.30

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
	height = 1 # We are currently only using blocks of height 1
	width = random.choice([2,4]) # The width can be 2 or 4

	if layer==0:
		x = 0 # Our first block is placed at the origin
		y = 0 # Our first block is placed at the origin
	else: # If this is not our first block...
		below = blockList[-1] # Obtain the block on the below layer, which should be the last placed in the list
		left = below.x-(width-1) # Obtain our leftmost possible location
		right = below.width+below.x - 1 # Obtain our rightmost possible location
		x = random.randrange(left,right+1) # The X coordinate is determined from Left and Right
		y = layer # The Y coordinate is the current layer
	color = random.choice([(255,0,0),(0,255,0),(0,0,255)]) # Find our color from these selections
	newBlock = LegoBlock(width,height,color,x,y) # Create our new block from the generated information
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

# TODO: Write this function
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

# Sends a default image for the introduction to the web server
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
	motion.setAngles("HeadPitch",0,0.1)
	tts.say(s)
	motion.setAngles("HeadPitch",HEADANGLE,0.1)

# This function continuously runs until there is 5 seconds of no motion on the camera. At this point, we may have the blocks on the board
# Need to keep into account a blank board and the initial blockList before the user removes the blocks from the board
# Returns nothing, Modifies nothing, No parameters
def waitForNoMotion():
	finTime = time.time() + 5 # 5 seconds
	while time.time()<=finTime:
		# Get 2 frames from /dev/video1
		pics = camera.takePictures(2,"/home/nao/NaoLego/","frame")
		frame1 = perspectiveCorrection(cv2.imread(pics[0][0]))
		frame2 = perspectiveCorrection(cv2.imread(pics[0][1]))
		# Resave our two frames
		cv2.imwrite("frame_0_p.jpg",frame1)
		cv2.imwrite("frame_1_p.jpg",frame2)
		# Compare the two frames
		if False: #cv2.norm(frame1,frame2,cv2.NORM_L1)>=10000:
			finTime = time.time() + 5

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
	pics = camera.takePictures(2,"/home/nao/NaoLego/","frame")
	img = cv2.imread(pics[0][0])
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
	return True

# -------------- MAIN -------------------------

# First thing, start our webserver
sendInitScreen()
thread.start_new_thread(webServerThread,())

# Prepare our camera
initCamera()

# Get the NAO in the correct position
posture.goToPosture("StandInit",1.0)
motion.setAngles("HeadPitch",HEADANGLE,0.1)

# Determine the points of our paper and our perspective
initPerspective()
			
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
for lcv in range(NUMBLOCKS-1): # -1 since we already placed 1 block
	addBlock()
	sendBlockList()
	NaoSay("Good Job. Now, please add this new block to the assembly.")
	waitForNoMotion()
	while not verifyBlocks:
		NaoSay("I'm sorry, that is not the correct block. Please place the block shown in the image.")
		waitForNoMotion()

sendFinScreen()
Finished = True
NaoSay("Great job! I hope you enjoyed this exercise! Come play again soon!")
