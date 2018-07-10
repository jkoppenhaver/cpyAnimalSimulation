# cpyAnimalSimulation
Simple Animal Simulation written in Adafruit's Circuit Python
## Overview
This project was meant to be a simple example of the Circuit Python languge and to show off Adafruit's Feather M0 Express board.
## Requirements
### Hardware
[Feather M0 Express](https://www.adafruit.com/product/3403)

[NeoPixel FeatherWing](https://www.adafruit.com/product/2945)
### Software
No IDE is needed because the Feather Express acts as a flashdrive and code can just be dropped on to it.  All that is needed is a text editor that can edit .py files.
#### Quick Start
1. Ensure that Circuit Python is installed on your board.  Intsructions for installing Circuit Python onto the board can be found [here](https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/kattni-circuitpython).
2. Download the python files in this repo.  There are multiple ways this can be done.
..+ Clone this repo to a local directory using the git clone command
..+ Download this repo as a .zip and extract the files.
3. Choose one of the examples to run.  Two demo files are provided, ocean.py and forest.py.  More information about the differences can be found in the [Full Description](#full-description).  Move whichever file you chose onto the CIRCUITPYTHON drive that shows up when you plug in your board.  If this drive does not show up, circuit python might not be properly installed.  Refer to step 1.
4. Rename the file you just moved to 'main.py'.  This tells the board which file it should run when it is powered on.
5. Move the animals.mpy file onto the CIRCUITPYTHON drive.  NOTE: *DO NOT* move the animals.py file to the CIRCUITPYTHON drive.  This file is provided incase you wish to change the animals class but only the precompiled animals.mpy file will run on the M0 board.  See the (Modifying the animals.py class)[#modifying-animals-class] section for more information.

#### Modifying the animals class
The animal class has become too large to run properly on the Feather M0 board so it must be precompiled to a .mpy file.  The precompiled animals.mpy file is provided and can be dropped onto the board, however, if any changes are made to animals.py, this file will need to be recompiled.  Instructions can be found [here](https://github.com/micropython/micropython/tree/master/mpy-cross) to use the mpy-cross tool to compile a new .mpy file.
## Full Description
This program uses colored dots on the NeoPixel Display to simulate predators and prey.  The prey move around the display randomly and the predator chases the closest prey.  If the predator catches the prey, the prey is removed from the display.  Two example files are provided as demonstrations.
### ocean.py
This program has one predator and many prey.  It has a blue background, one white shark, and four orange fish.  The shark will chase the fish until they are all gone and then it will roam the map randomly.

![](https://i.imgur.com/Qom8eBt.gif)
### forest.py
This program has two predators and many prey.  It has a green background, one red wolf, one yellow bear, and four white rabbits.  The wolf and bear will chase the rabbits until they are all gone and then they will roam the map randomly.  This program demonstrates that it is possible to have two predators that do on chase or interact with each other.

![](https://i.imgur.com/XFh5fHI.gif)