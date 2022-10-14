import unittest

from AstroCal.control.control import getDateOfNextNewMoon

class TestDateOfNextNewMoon(unittest.TestCase):
    def test_DaysTillFullMoon_WhenSuccessful(self):
        test_result = getDateOfNextNewMoon(2022,10,4)
        self.assertEqual((test_result[0], test_result[1], test_result[2]),(2022,10,25),"Test Fail")
        test_result = getDateOfNextNewMoon(2032,12,8)
        self.assertEqual((test_result[0], test_result[1], test_result[2]),(2033,1,1),"Test Fail")

    def test_DateOfNextNewMoon_WhenUnsuccessful(self):
        self.assertNotEqual(getDateOfNextNewMoon(2022,10,4),(2022,10,24),"Test Fail")
        self.assertNotEqual(getDateOfNextNewMoon(2022,10,4),(2022,10,26),"Test Fail")
        self.assertNotEqual(getDateOfNextNewMoon(2032,12,8),(2032,12,31),"Test Fail")
        self.assertNotEqual(getDateOfNextNewMoon(2032,12,8),(2033,1,2),"Test Fail")
