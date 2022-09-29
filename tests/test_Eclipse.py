import unittest

#sys.path.insert(1, 'AstroCal\control')
#import control
#from AstroCal import control
from AstroCal.control.control import getWhenSolEclipseLoc

class TestEclipse(unittest.TestCase):
    def test_SolEcl_When(self):
        self.assertEqual(getWhenSolEclipseLoc(2022,9,27),(2023, 10, 14, 15, 9, 15.699218809604645),"Test Fail")
    
        


if __name__ == '__main__':
    unittest.main()