#!/usr/bin/env python3

import os
import subprocess
import tkinter as tk
from tkinter import colorchooser, messagebox, ttk

root = tk.Tk()

# Global variables
font = 'fixed'
font_size = 12
fg_color = 'black'
bg_color = 'white'
log_var = tk.BooleanVar()
geometry_var = tk.StringVar(value='80x24')


def read_xterm_config():
    x_cols = 80
    x_rows = 24
    x_sl = 200
    x_fn = '9x15bold'
    x_bg = 'DarkGrey'
    x_fg = 'Navy'
    log = 0
    xpath = '/usr/bin'

    xtrc_file = os.path.expanduser('~/.xtrc')
    if os.path.exists(xtrc_file):
        with open(xtrc_file) as f:
            for line in f:
                line = line.strip()
                if not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    if key == 'x_cols':
                        x_cols = int(value)
                    elif key == 'x_rows':
                        x_rows = int(value)
                    elif key == 'x_sl':
                        x_sl = int(value)
                    elif key == 'x_fn':
                        x_fn = value
                    elif key == 'x_bg':
                        x_bg = value
                    elif key == 'x_fg':
                        x_fg = value
                    elif key == 'log':
                        log = int(value)
                    elif key == 'xpath':
                        xpath = value
    return x_cols, x_rows, x_sl, x_fn, x_bg, x_fg, log, xpath

def run_xterm(font_size, geometry, bg, fg, log):
    if not os.environ.get('DISPLAY'):
        print('Error: DISPLAY environment variable is not set')
        return

    x_cols, x_rows, x_sl, x_fn, x_bg, x_fg, log, xpath = read_xterm_config()
    xterm = os.path.join(xpath, 'xterm')

    if x_bg:
        xt_command = f"{xterm} -bg {x_bg}"

    if x_fg:
        xt_command += f" -fg {x_fg}"

    if x_sl:
        xt_command += f" -sl {x_sl}"

    geometry = str(x_cols) + "x" + str(x_rows) + "+100+100"
    if geometry:
        xt_command += f" -geometry {geometry}"

    if font_size:
        xt_command += f" -fs {x_fn}"

    if log:
        xt_command += " -l"

    xt_command += " -e /bin/ksh"

    print("DEBUG:\n" + str(xt_command) + "\n")
    #os.environ['XMODIFIERS'] = ''
    os.environ['XMODIFIERS'] = '@im=none'
    os.environ['LANG'] = 'en_US.UTF-8'
    os.environ['LC_ALL'] = 'en_US.UTF-8'
    os.system(xt_command)

def set_font(value):
    global font
    font = value

def set_font_size(value):
    global font_size
    font_size = value

def set_fg_color():
    global fg_color
    fg_color = colorchooser.askcolor()[1]

def set_bg_color():
    global bg_color
    bg_color = colorchooser.askcolor()[1]


def create_xterm():
    # Create the Tk object and start the main loop
    root = tk.Tk()
    root.title('xt')

    # Set up variables for font size, foreground color, and background color
    font_size_var = tk.StringVar(root, '10')
    fg_color_var = tk.StringVar(root, '#ffffff')
    bg_color_var = tk.StringVar(root, '#000000')
    log_var = tk.BooleanVar()

    # Create widgets for font size, foreground color, and background color
    font_size_label = tk.Label(root, text='Font size:')
    font_size_entry = tk.Entry(root, textvariable=font_size_var)
    fg_color_label = tk.Label(root, text='Foreground color:')
    fg_color_entry = tk.Entry(root, textvariable=fg_color_var)
    bg_color_label = tk.Label(root, text='Background color:')
    bg_color_entry = tk.Entry(root, textvariable=bg_color_var)
    log_checkbutton = tk.Checkbutton(root, text='Log output', variable=log_var)

    # Create buttons for standard color combinations
    buttons_frame = tk.Frame(root)
    colors = [
        ('#000000', '#ffffff'), ('#ffffff', '#000000'), ('#008000', '#ffffff'),
        ('#ffff00', '#000000'), ('#0000ff', '#ffffff'), ('#ff0000', '#ffffff'),
        ('#00ffff', '#000000'), ('#ff00ff', '#ffffff'), ('#808080', '#ffffff'),
        ('#c0c0c0', '#000000'), ('#008080', '#ffffff'), ('#ff8040', '#ffffff'),
        ('#00ff00', '#000000'), ('#800080', '#ffffff'), ('#804000', '#ffffff'),
        ('#ff80ff', '#000000')
    ]
#    for i, (fg_color, bg_color) in enumerate(colors):
#        button = tk.Button(
#            buttons_frame,
#            text=f'Button {i+1}',
#            fg=fg_color,
#            bg=bg_color,
#            command=lambda fg=fg_color, bg=bg_color: run_xterm(
#                font_size_var.get(), fg, bg, log_var.get()
#            )
#        )
    for i, (fg_color, bg_color) in enumerate(colors):
        button = tk.Button(
            buttons_frame,
            text=f'Button {i+1}',
            fg=fg_color,
            bg=bg_color,
            command=lambda fg=fg_color, bg=bg_color: run_xterm(
                font_size_var.get(), 
                geometry_var.get(), 
                bg_color, 
                fg_color, 
                log_var.get()
            )
        )

        button.pack(side='left')

    # Pack all the widgets into the root window
    font_size_label.pack(side='left')
    font_size_entry.pack(side='left')
    fg_color_label.pack(side='left')
    fg_color_entry.pack(side='left')
    bg_color_label.pack(side='left')
    bg_color_entry.pack(side='left')
    log_checkbutton.pack(side='left')
    buttons_frame.pack()

    root.mainloop()

def toggle_logging():
    global log_var
    log_option = '-l' if log_var.get() else ''

def main():
    # Set up the main window
    root = tk.Tk()
    root.title('XTerm Dashboard')

    # Create font selector
    font_frame = ttk.Frame(root, padding=10)
    font_frame.pack(fill=tk.X)

    font_label = ttk.Label(font_frame, text='Font:', padding=5)
    font_label.pack(side=tk.LEFT)

    font_box = ttk.Combobox(font_frame, values=['fixed', '9x15', 'courier', 'lucidatypewriter'], state='readonly')
    font_box.pack(side=tk.LEFT)
    font_box.current(0)
    font_box.bind("<<ComboboxSelected>>", lambda event: set_font(font_box.get()))

    # Create font size selector
    size_frame = ttk.Frame(root, padding=10)
    size_frame.pack(fill=tk.X)

    size_label = ttk.Label(size_frame, text='Font size:', padding=5)
    size_label.pack(side=tk.LEFT)

    size_box = ttk.Combobox(size_frame, values=['12', '14', '16', '18', '20'], state='readonly')
    size_box.pack(side=tk.LEFT)
    size_box.current(0)
    size_box.bind("<<ComboboxSelected>>", lambda event: set_font_size(size_box.get()))

    # Create foreground color selector
    fg_frame = ttk.Frame(root, padding=10)
    fg_frame.pack(fill=tk.X)

    fg_label = ttk.Label(fg_frame, text='Foreground color:', padding=5)
    fg_label.pack(side=tk.LEFT)

    fg_button = ttk.Button(fg_frame, text='Choose', command=set_fg_color)
    fg_button.pack(side=tk.LEFT)

    # Create background color selector
    bg_frame = ttk.Frame(root, padding=10)
    bg_frame.pack(fill=tk.X)

    bg_label = ttk.Label(bg_frame, text='Background color:', padding=5)
    bg_label.pack(side=tk.LEFT)

    bg_button = ttk.Button(bg_frame, text='Choose', command=set_bg_color)
    bg_button.pack(side=tk.LEFT)

    # Create log checkbox
    log_frame = ttk.Frame(root, padding=10)
    log_frame.pack(fill=tk.X)

    log_label = ttk.Label(log_frame, text='Enable logging:', padding=5)
    log_label.pack(side=tk.LEFT)

    log_box = ttk.Checkbutton(log_frame, variable=log_var, command=toggle_logging)
    log_box.pack(side=tk.LEFT)

    # Create button frame
    button_frame = ttk.Frame(root, padding=10)
    button_frame.pack
    
# Create main window
root = tk.Tk()
root.title("xterm Dashboard")

# Create font selection widgets
font_label = tk.Label(root, text="Select font:")
font_label.grid(row=0, column=0)

font_box = tk.Entry(root)
font_box.insert(0, "fixed")
font_box.grid(row=0, column=1)

font_size_label = tk.Label(root, text="Select font size:")
font_size_label.grid(row=1, column=0)

font_size_box = tk.Entry(root)
font_size_box.insert(0, "10")
font_size_box.grid(row=1, column=1)

# Create color selection widgets
fg_color_label = tk.Label(root, text="Select foreground color:")
fg_color_label.grid(row=2, column=0)

fg_color_box = tk.Entry(root)
fg_color_box.insert(0, "black")
fg_color_box.grid(row=2, column=1)

bg_color_label = tk.Label(root, text="Select background color:")
bg_color_label.grid(row=3, column=0)

bg_color_box = tk.Entry(root)
bg_color_box.insert(0, "white")
bg_color_box.grid(row=3, column=1)

# Create logging option widget
log_var = None
log_checkbutton = tk.Checkbutton(root, text="Enable logging", variable=log_var)
log_checkbutton.grid(row=4, column=0, columnspan=2)

# Create launch button
launch_button = tk.Button(root, text="Launch xterm", command=create_xterm)
launch_button.grid(row=5, column=0, columnspan=2)

# Start GUI event loop
root.mainloop()
