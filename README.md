# cpyForestSimulation
Simple Animal Simulation written in Adafruit's Circuit Python
## Overview
This project was meant to be a simple example of the Circuit Python languge and to show off Adafruit's Feather M0 Express board.
## Requirements
### Hardware
[Feather M0 Express](https://www.adafruit.com/product/3403)
[NeoPixel FeatherWing](https://www.adafruit.com/product/2945)
### Software
No IDE is needed because the Feather Express acts as a flashdrive and code can just be dropped on to it.  All that is needed is a text editor that can edit .py files.  Intsructions for installing Circuit Python onto the board can be found [here](https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/kattni-circuitpython).
## Full Description
This program uses colored dots on the NeoPixel Display to simulate predators and prey.  The prey move around the display randomly and the predator chases the closest prey.  If the predator catches the prey, the prey is removed from the display.