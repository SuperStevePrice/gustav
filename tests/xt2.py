#!/bin/bash

# Read the X resources file
xrdb -load ~/.Xresources

# Launch xterm with the appropriate options
xterm -bg "$background" -fg "$foreground" -fn "$font"

