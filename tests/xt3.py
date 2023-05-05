#!/usr/bin/env python3

import os

# get path to user's home directory
home_dir = os.path.expanduser("~")

# build path to .Xresources file
xresources_path = os.path.join(home_dir, ".Xresources")

# read contents of .Xresources file
try:
    with open(xresources_path, "r") as f:
        xresources = f.read()
    print(f"Contents of .Xresources:\n{xresources}")
except FileNotFoundError:
    print(".Xresources file not found")
    
# launch xterm window
os.system("xterm")

