import os
import sys
from sys import platform
script_dir = os.path.dirname( __file__ )
path = os.path.join(script_dir, '..')
sys.path.insert(0, path)
import core
core.run()