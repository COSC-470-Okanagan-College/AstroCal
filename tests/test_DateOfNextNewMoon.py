import unittest

from control import getDateOfNextNewMoon

class TestDateOfNextNewMoon(unittest.TestCase):
    def test_DaysTillFullMoon_WhenSuccessful(self):
        self.assertEqual(getDateOfNextNewMoon(2022,10,4),(2022,10,25),"Test Fail")
        self.assertEqual(getDateOfNextNewMoon(2032,12,8),(2033,1,1),"Test Fail")

    def test_DateOfNextNewMoon_WhenUnsuccessful(self):
        self.assertNotEqual(getDateOfNextNewMoon(2022,10,4),(2022,10,24),"Test Fail")
        self.assertNotEqual(getDateOfNextNewMoon(2022,10,4),(2022,10,26),"Test Fail")
        self.assertNotEqual(getDateOfNextNewMoon(2032,12,8),(2032,12,31),"Test Fail")
        self.assertNotEqual(getDateOfNextNewMoon(2032,12,8),(2033,1,2),"Test Fail")


if __name__ == '__main__':
    unittest.main()