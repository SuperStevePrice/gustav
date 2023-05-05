#!/usr/bin/env python3
import os
os.environ["XTERM_LOCALE"] = "UTF-8"

#Merge the resources in ~/.Xresources with the current resources in the X server
os.system("xrdb -merge ~/.Xresources")

# Set the xterm resources
os.environ['XTERM_GEOMETRY'] = '80x45+10+10'
os.environ['XTERM_FONT'] = 'xft:Monospace:pixelsize=12'
os.environ['XTERM_FONT'] = '9x15bold'
os.environ['FOREGROUND'] = 'white'
os.environ['BACKGROUND'] = 'DarkGreen'

# Disable input methods
os.environ['XMODIFIERS'] = '@im=none'

print(f"xterm parameters: -geometry {os.environ['XTERM_GEOMETRY']} -fn {os.environ['XTERM_FONT']} -bg {os.environ['BACKGROUND']} -fg {os.environ['FOREGROUND']}")
print(f"XTERM_FONT value: {os.environ['XTERM_FONT']}")

# Launch xterm with the specified resources
os.system("xterm -u8 -geometry $XTERM_GEOMETRY -fn $XTERM_FONT -bg $BACKGROUND -fg $FOREGROUND")
