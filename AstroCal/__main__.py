import os
import sys

def show_help():
	print("Available options:\n--TUI - Runs the application as a terminal interface.\n--GUI Runs the application as a graphical user interface with fewer features.")

# Add AstroCal directory to Python path
# Fixes our AstroCal.[...] imports
script_dir = os.path.dirname( __file__ )
path = os.path.join(script_dir, '..')
sys.path.insert(0, path)

n = len(sys.argv)
use_terminal = False
use_GUI = True
for i in range (1, n):
	opt = sys.argv[i]
	if opt == "--TUI":
		use_terminal = True
		use_GUI = False
	elif opt == "--GUI":
		use_terminal = False
		use_GUI = True
	elif opt == "--help":
		show_help()
		exit()
	else:
		print("Unsupported option: " + opt)
		show_help()
		exit(1)


# Remove any command line options as they confuse Kivy
sys.argv = sys.argv[0:1]

import core
if use_terminal:
	core.run_TUI()
elif use_GUI:
	core.run_GUI()
