#!/usr/bin/env python3

import os

# Merge the resources in ~/.Xresources with the current resources in the X server
os.system("xrdb -merge ~/.Xresources")

# Launch xterm with the specified resources
os.system("xterm")

