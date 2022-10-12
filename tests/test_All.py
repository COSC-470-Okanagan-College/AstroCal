import os
import sys
from sys import platform
script_dir = os.path.dirname( __file__ )
path = os.path.join(script_dir, '..')
sys.path.insert(0, path)
import unittest

import test_DaysTillNextFullMoon
import test_Eclipse
import test_DateOfNextNewMoon
import test_sanitizeInputs

# Added the files for each test in here with a corresponding "run" command
suite = unittest.TestLoader().loadTestsFromModule(test_DaysTillNextFullMoon)
unittest.TextTestRunner(verbosity=1).run(suite)
suite = unittest.TestLoader().loadTestsFromModule(test_Eclipse)
unittest.TextTestRunner(verbosity=1).run(suite)
suite = unittest.TestLoader().loadTestsFromModule(test_DateOfNextNewMoon)
unittest.TextTestRunner(verbosity=1).run(suite)
suite = unittest.TestLoader().loadTestsFromModule(test_sanitizeInputs)
unittest.TextTestRunner(verbosity=1).run(suite)
