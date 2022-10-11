import unittest

import test_DaysTillNextFullMoon
import test_Eclipse
import test_DateOfNextNewMoon

# Added the files for each test in here with a corresponding "run" command
suite = unittest.TestLoader().loadTestsFromModule(test_DaysTillNextFullMoon)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromModule(test_Eclipse)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromModule(test_DateOfNextNewMoon)
unittest.TextTestRunner(verbosity=2).run(suite)