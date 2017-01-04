#! /usr/bin/python

# TODO: Write function verifyBlocks
# TODO: Obtain data such as time to add block, number of incorrect blocks, and individual error counters for wrong coordinates, wrong color, wrong size, etc.
# TODO: At the end of the program, save the obtained data to a CSV file for future processing.

from LegoBlock import LegoBlock
from naoqi import ALProxy
from naoqi import ALBroker
from HeadTouch import HeadTouch
import SimpleHTTPServer
import SocketServer
import os
from shutil import copyfile
import time
import thread
import random
import numpy as np
import cv2
import sys
import math

SERVERPORT = 8080 # What port number with the hosted webserver be run on?
NUMBLOCKS = 5 # Represents the number of blocks we will assemble
IP = "127.0.0.1" # IP Address of the Nao. Since this is run from the Nao, this is localhost
tts = ALProxy("ALTextToSpeech",IP,9559) # Handles speech from the Nao
motion = ALProxy("ALMotion",IP,9559) # Handles joint movements for the Nao
posture = ALProxy("ALRobotPosture",IP,9559) # Handles postures of the robot
camera = ALProxy("ALPhotoCapture",IP,9559) # Handles the camera of the robot
audio = ALProxy("ALAudioPlayer",IP,9559) # Handles sound output
myBroker = ALBroker("myBroker","0.0.0.0",0,IP,9559)
HeadTouch = HeadTouch("HeadTouch")
Finished = False
perspective_mat = None # Holds the transformation matrix for the visual perspective
HEADANGLE = 0.28 # Calibrated so he does not see his feet

# What lego blocks do we have?
presentBlockList = [] # Represents the list of LegoBlocks we actually have
red4x1 = LegoBlock(4,1,(0,0,200),0,0)
green4x1 = LegoBlock(4,1,(0,180,0),0,0)
blue4x1a = LegoBlock(4,1,(220,110,0),0,0)
blue4x1b = LegoBlock(4,1,(220,110,0),0,0)
blue4x1c = LegoBlock(4,1,(220,110,0),0,0)
blue4x1d = LegoBlock(4,1,(220,110,0),0,0)
red2x1a = LegoBlock(2,1,(0,0,200),0,0)
red2x1b = LegoBlock(2,1,(0,0,200),0,0)
green2x1a = LegoBlock(2,1,(0,180,0),0,0)
green2x1b = LegoBlock(2,1,(0,180,0),0,0)
green2x1c = LegoBlock(2,1,(0,180,0),0,0)
blue2x1a = LegoBlock(2,1,(220,110,0),0,0)
blue2x1b = LegoBlock(2,1,(220,110,0),0,0)
presentBlockList.append(red4x1)
presentBlockList.append(green4x1)
presentBlockList.append(blue4x1a)
presentBlockList.append(blue4x1b)
presentBlockList.append(blue4x1c)
presentBlockList.append(blue4x1d)
presentBlockList.append(red2x1a)
presentBlockList.append(red2x1b)
presentBlockList.append(green2x1a)
presentBlockList.append(green2x1b)
presentBlockList.append(green2x1c)
presentBlockList.append(blue2x1a)
presentBlockList.append(blue2x1b)
random.shuffle(presentBlockList) # Shuffle our presentBlockList

blockList = [] # Represents a list of LegoBlocks. Is initialized as empty

# Initializes the camera settings
def initCamera():
	camera.setResolution(2)
	camera.setPictureFormat("jpg")
	camera.setCameraID(1)

# Plays the audio file given as a parameter
def playAudio(file):
	fileID = audio.loadFile(file)
	audio.play(fileID)

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
# Will not place a new block of the same color as the previous block, to improve CV recognition
def addBlock():
	# Find the current layer
	layer = 0
	for block in blockList:
		layer += block.getHeight() # Increase Layer by the height of the block
	width = 0
	height = 0
	if layer==0:
		# Ensure that our first block is 4 long
		while presentBlockList[-1].getWidth()==2:
			random.shuffle(presentBlockList)
		newBlock = presentBlockList.pop() # Get a new block from our presentBlockList
		height = newBlock.getHeight()
		width = newBlock.getWidth()
		newBlock.setCoords(0,0) # Our first block is placed at the origin
	else: # If this is not our first block...
		prevcolor = blockList[-1].getColor()
		nextcolor = presentBlockList[-1].getColor()
		while prevcolor==nextcolor or (layer==1 and presentBlockList[-1].getWidth()==4) or (layer>1 and blockList[-2].getColor()==nextcolor):
			random.shuffle(presentBlockList)
			nextcolor = presentBlockList[-1].getColor()
		newBlock = presentBlockList.pop()
		height = newBlock.getHeight()
		width = newBlock.getWidth()
		below = blockList[-1] # Obtain the block on the below layer, which should be the last placed in the list
		left = below.x-(width-1) # Obtain our leftmost possible location
		right = below.width+below.x - 1 # Obtain our rightmost possible location
		newx = random.randrange(left,right+1)
		if layer==1:
			newx = random.randrange(0,3)
		newBlock.setCoords(newx,layer) # The X coordinate is determined from Left and Right, The Y coordinate is the current layer
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

# Creates an image of the blockList and sends it out to a web server
# No returns, No parameters, No variable modifications, Modifies the image file for the web server (image.jpg)
def sendBlockList():
	imW = 640 # image width
	imH = 480 # image height
	xUnit = imW / 20 # one Lego block unit in width
	yUnit = imH / 15 # one Lego block unit in height
	xOff = (imW / 2) - ((imW / xUnit) * 8) # offset along x-axis for where to begin drawing blocks
	yOff = (imH / 2) - ((imH / yUnit) * 3) # offset along y-axis for where to begin drawing blocks
	nubW = xUnit - xUnit / 2 # nub width
	nubH = yUnit - yUnit / 2 # nub height
	nubXOff = nubW / 2 # nub x-axis offset for where to begin drawing nub
	img = np.zeros((imH,imW,3),dtype=np.uint8)
	img.fill(255)
	for block in blockList:
		y = (block.y * yUnit) + yOff
		for x in range(block.x, block.x + block.width):
			curX = (x * xUnit) + xOff
			top_L = (curX, y)
			bot_R = (top_L[0]+xUnit-1, top_L[1]+yUnit-1)
			cv2.rectangle(img, top_L, bot_R, block.color, -1)
			top_L = (top_L[0]+nubXOff, bot_R[1])
			bot_R = (top_L[0]+nubW, top_L[1]+nubH)
			cv2.rectangle(img, top_L, bot_R, block.color, -1)
	res = cv2.flip(img,0)
	cv2.imwrite('image.jpg', res)


def sendCVBlockList():
	imW = 640 # image width
	imH = 480 # image height
	xUnit = imW / 20 # one Lego block unit in width
	yUnit = int(xUnit * 0.6) # one Lego block unit in height
	yUnitPlus = int(yUnit * 0.66)
	xOff = (imW / 2) - ((imW / xUnit) * 8) # offset along x-axis for where to begin drawing blocks
	yOff = (imH / 2) - ((imH / yUnit) * 3) # offset along y-axis for where to begin drawing blocks
	nubW = int(xUnit * 0.75) # nub width
	nubH = int(yUnit * 1.6667) # nub height
	nubXOff = int(nubW - (nubW * 0.8125) ) # nub x-axis offset for where to begin drawing nub
	img = np.zeros((imH, imW, 3), dtype=np.uint8)
	img.fill(255)
	for block in blockList:
		y = (block.y * yUnit) + yOff
		for x in range(block.x, block.x + block.width):
			# Draw shadowed perspective
			curX = (x * xUnit) + xOff
			top_L = (curX, y)
			bot_R = (top_L[0]+xUnit-1, top_L[1]+yUnit+yUnitPlus-1)
			cv2.rectangle(img, top_L, bot_R, tuple([0.6*x for x in block.color]), -1)
			# Draw block
			bot_R = (top_L[0]+xUnit-1, top_L[1]+yUnit-1)
			cv2.rectangle(img, top_L, bot_R, block.color, -1)
			# Draw nub
			top_L = (curX+nubXOff, bot_R[1])
			bot_R = (top_L[0]+nubW, top_L[1]+nubH)
			cv2.rectangle(img, top_L, bot_R, block.color, -1)
	res = cv2.flip(img,0)
	cv2.imwrite('cvblocklist.jpg', res)

# Sends a default image for the introduction of the application
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)
# Just need to remove image.jpg and copy resources/init_screen.jpg to image.jpg.
def sendInitScreen():
	if os.path.isfile('image.jpg'):
		os.remove('image.jpg')
	copyfile('resources/init_screen.jpg','image.jpg')

# Sends an image for the finished program to the web server
# No returns, no parameters, no varaible modifications, Modifies the image file for the web server (image.jpg)Nao
# Just need to remove image.jpg and copy resources/fin_screen.jpg to image.jpg.
def sendFinScreen():
	if os.path.isfile('image.jpg'):
		os.remove('image.jpg')
	copyfile('resources/fin_screen.jpg','image.jpg')

# Tells the NAO to say a message. Takes the message as a string parameters. No returns or modifications
# Moves his head to look at the user while talking
def NaoSay(s):
	motion.setAngles("HeadPitch",0,0.1) # Look at the user
	tts.say(s) # Say our message
	motion.setAngles("HeadPitch",HEADANGLE,0.1) # Return to board

# The nao will prompt the user and wait until his head receives contact
def waitForHeadTouch():
	global HeadTouch
	tts.say("Please touch my head when you are ready.")
	HeadTouch.resetTouched();
	while not HeadTouch.isTouched():
		time.sleep(0.25)
	playAudio("/home/nao/NaoLego/resources/ack.wav") # Play an audio file to acknowledge the head touch

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

# Verify that our perspective points are correct, as best we can
def verifyPerspectivePoints(pts):
	# Convert points from lists to tuples
	pts_tuples = [(v[0],v[1]) for v in pts.tolist()]
	# Ensure we do not have any duplicate points
	if not len(set(pts_tuples))==len(pts_tuples):
		return False
	# Can implement more verifications here in the future
	return True

# Obtain an image of the blank paper and determine our critical points and our perspective matrix
def initPerspective():
	global perspective_mat
	pic = camera.takePicture("/home/nao/NaoLego/","frame")
	img = cv2.imread(pic[0])
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(gray,4,0.01,10)
	corners = np.float32([corners[0][0],corners[1][0],corners[2][0],corners[3][0]])
	perspective_pts = order_points(corners)
	if not verifyPerspectivePoints(perspective_pts):
		print "ERROR! MAY BE INVALID PERSPECTIVE POINTS!"
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

# pt1 and pt2 represent out created image
# pt3 and pt4 represent our camera image
def getAffineTransform(pt1,pt2,pt3,pt4):
	pt1x,pt1y = pt1
	pt2x,pt2y = pt2
	pt3x,pt3y = pt3
	pt4x,pt4y = pt4
	scale = math.sqrt(((pt4y-pt3y)**2)+((pt4x-pt3x)**2))/(pt2x-pt1x)
	theta = -1*math.atan((pt4y-pt3y)/(pt4x-pt3x))
	centerx = pt1x
	centery = pt1y
	a = scale*math.cos(theta)
	b = scale*math.sin(theta)
	M = np.float32([[a,b,(1-a)*centerx - b*centery],[-b,a,b*centerx+(1-a)*centery]])
	return M


# TODO: Write this function
# This function verifies that the blocks on the board match the blockList. Returns either True or False, with True being a match
# No parameters, No modifications
def verifyBlocks():
	pic = camera.takePicture("/home/nao/NaoLego/","frame")
	img = perspectiveCorrection(cv2.imread(pic[0])) # Apply perspective correction to our image
	# Flip the picture to an orientation matching our generated image
	img = cv2.flip(img,1)
	img = cv2.flip(img,0)
	cv2.imwrite("frameP.jpg",img) # Save our new perspectivized image to frameP.jpg
	l = sendCVBlockList() # Save our expected image to cvblocklist.jpg, return focus points
	exp_img = cv2.imread("cvblocklist.jpg") # Load our expected image to exp_img variable
	
	# Use thresholding to bitmask background away from img
	cols,rows = (480,640)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	thresh_inv = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
	thresh = cv2.bitwise_not(thresh_inv) # Flip our threshold around
	mask_bgr = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
	img = cv2.bitwise_and(img,mask_bgr)
	img = cv2.addWeighted(img,1,cv2.cvtColor(thresh_inv,cv2.COLOR_GRAY2BGR),1,0)
	
	# At this point, img is our white-background perspectivized camera
	# exp_img is our created image
	
	# Get pt1 and pt2 from our created image TODO: Actual returned values
	pt1 = (160,314) #l[0]
	pt2 = (287,314) #l[1]
	
	# TODO: Determine bottom two corners of blocks in img (pt3, pt4)
	pt3 = (162,433)
	pt4 = (473,445)
	
	# Rotate/Scale to match corners between exp_img and img, adjusting exp_img
	M = getAffineTransform(pt1,pt2,pt3,pt4)
	N = np.float32([[1,0,pt3[0]-pt1[0]],[0,1,pt3[1]-pt1[1]]])
	exp_img = cv2.warpAffine(exp_img,M,(rows,cols)) # Rotate and scale our image
	exp_img = cv2.warpAffine(exp_img,N,(rows,cols)) # Translate our image
	exp_img[np.where((exp_img==[0,0,0]).all(axis=2))] = [255,255,255] # Turn background white, rather than black
	n = cv2.norm(exp_img,img,cv2.NORM_L2)
	d = cv2.absdiff(img,exp_img)
	cv2.imwrite("diff.jpg",d)
	NaoSay("The Norm is " + str(int(n))) # Relay the floored norm back to the user
	
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
initPerspective() # Find our perspective transformation
verifyBlocks() # Go ahead and obtain an image from the camera so we aren't looking at a previous picture

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
playAudio("/home/nao/NaoLego/resources/clap.wav")
NaoSay("Great job! I hope you enjoyed this exercise! Come play again soon!")
myBroker.shutdown()
sys.exit(0)
