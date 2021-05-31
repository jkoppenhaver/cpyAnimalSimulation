import neopixel
import board
import time
import Animals

SHARK_COLOR = (30, 30, 30)
FISH_COLOR = (80, 40, 0)
BLANK_COLOR = (0, 0, 10)

# Initialize and turn off the on board RGB LED
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
dot[0] = (0, 0, 0)

# Initialize the NeoPixel FeatherWing
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
# Description: This function converts the 2D display buffer to the 1D array the
#             NeoPixels use and writes the values to the display.
# Arguments: None
# Returns: Nothing
###############################################################################
def updateDisplay():
    global pdata
    for i in range(len(pdata)):
        for j in range(len(pdata[i])):
            disp[(j * 8) + i] = pdata[i][j]
    disp.show()
    return


# Clear the Display
updateDisplay()
# Generate one wolf and one bear
predators = [Animals.Predator(SHARK_COLOR, BLANK_COLOR, FISH_COLOR, pdata)]
# Generate a list to hold all of the rabbits and add a bunch of them
prey = [Animals.Prey(FISH_COLOR, BLANK_COLOR, pdata), Animals.Prey(FISH_COLOR, BLANK_COLOR, pdata),
        Animals.Prey(FISH_COLOR, BLANK_COLOR, pdata), Animals.Prey(FISH_COLOR, BLANK_COLOR, pdata)]
# Update the display to show all of the newly created animals
updateDisplay()
while True:
    # Move all the remaining rabbits
    for p in prey:
        p.move(pdata)
    # Update the display to show the rabbits movement and wait for a little before moving the wolves
    updateDisplay()
    time.sleep(0.5)
    # Move the predators
    for predator in predators:
        predator.move(pdata)
        # Check to see if any prey were caught and remove them if they have been
        for i in range(len(prey)):
            if predator.prey == prey[i].color:
                if (predator.x == prey[i].x) and (predator.y == prey[i].y):
                    prey.pop(i)
                    break
    # Update the display to show the movement and wait for a little before moving the prey again
    updateDisplay()
    time.sleep(0.3)
