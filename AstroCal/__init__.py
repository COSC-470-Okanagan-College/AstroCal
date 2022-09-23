from core import run
import sys

# Check for minimum version of Python (3.10)
MIN_PYTHON = (3, 10)
if sys.version_info < MIN_PYTHON:
	sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

run()