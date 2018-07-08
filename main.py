import neopixel
import board
import time
import Animals

WOLF_COLOR = (255,0,0)
BEAR_COLOR = (127,127,0)
RABBIT_COLOR = (40,40,20)
BLANK_COLOR = (0,10,0)

# Initialize and turn off the on board RGB LED
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
dot[0] = (0,0,0)

# Initilize the NeoPixel FeatherWing
# It has 32 LEDs and is by default connected to Pin D6
disp = neopixel.NeoPixel(board.D6, 32, brightness=0.2, auto_write=False)

# Create a display buffer to hold the pixel data
# This is a 2D array that more accurately represents the pixel layout
#  then the long 1D array of NeoPixles
# The FeatherWing is 4 LEDs tall and 8 wide
# Fill the buffer with the blank color
h = 4
w = 8
pdata = [[BLANK_COLOR for i in range(h)] for j in range(w)]

###############################################################################
# updateDisplay()
# Descrption: This function converts the 2D display buffer to the 1D array the
#             NeoPixels use and writes the values to the display.
# Arguments: None
# Returns: Nothing
###############################################################################
def updateDisplay():
	global pdata
	for i in range(len(pdata)):
		for j in range(len(pdata[i])):
			disp[(j*8)+i] = pdata[i][j]
	disp.show()
	return
	
#Clear the Display
updateDisplay()
#Generate one wolf and one bear
wolf = Animals.Predator(WOLF_COLOR, BLANK_COLOR, RABBIT_COLOR, pdata)
bear = Animals.Predator(BEAR_COLOR, BLANK_COLOR, RABBIT_COLOR, pdata)
#Generate a list to hold all of the rabbits and add a bunch of them
rabbits = []
rabbits.append(Animals.Prey(RABBIT_COLOR, BLANK_COLOR, pdata))
rabbits.append(Animals.Prey(RABBIT_COLOR, BLANK_COLOR, pdata))
rabbits.append(Animals.Prey(RABBIT_COLOR, BLANK_COLOR, pdata))
rabbits.append(Animals.Prey(RABBIT_COLOR, BLANK_COLOR, pdata))
# Update the display to show all of the newly created animals
updateDisplay()
while(True):
	# Check to see if any rabbits have been eaten and remove them if they have been
	for i in range(len(rabbits)):
		if(wolf.x == rabbits[i].x) and (wolf.y == rabbits[i].y) or (bear.x == rabbits[i].x) and (bear.y == rabbits[i].y):
			rabbits.pop(i)
			break
	# Move all the remaining rabbits
	for rabbit in rabbits:
		rabbit.move(pdata)
	# Update the display to show the rabbits movement and wait for a little before moving the wolves
	updateDisplay()
	time.sleep(0.5)
	# Move the predators
	wolf.move(pdata)
	bear.move(pdata)
	# Update the display to show the wolf's movement and wait for a little before moving the rabbits again
	updateDisplay()
	time.sleep(0.3)