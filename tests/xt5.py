#!/usr/bin/env python3

import os

# Merge the resources in ~/.Xresources with the current resources in the X server
os.system("xrdb -merge ~/.Xresources")

# Set the xterm resources
os.environ['XTERM_GEOMETRY'] = '80x24+10+10'
#os.environ['XTERM_FONT'] = 'xft:Monospace:pixelsize=12'
#os.environ['XTERM_ROWS'] = '24'
#os.environ['XTERM_COLUMNS'] = '80'
os.environ['FOREGROUND'] = 'white'
os.environ['BACKGROUND'] = 'DarkGreen'

# Launch xterm with the specified resources
os.system("xterm -geometry $XTERM_GEOMETRY -fn $XTERM_FONT -bg $BACKGROUND -fg $FOREGROUND")
