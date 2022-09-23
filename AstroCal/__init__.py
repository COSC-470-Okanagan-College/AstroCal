from core import run
import sys

# Check for minimum version of Python (3.8)
MIN_PYTHON = (3, 8)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

run()

# test change