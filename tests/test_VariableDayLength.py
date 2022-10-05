import unittest

from control import getVariableDayLength

class TestDayLength(unittest.TestCase):
    def test_DayLength_WhenSuccessful(self):
        self.assertEqual(getVariableDayLength(2022,10,4,1),[[11,27]],"Test Fail")
        self.assertEqual(getVariableDayLength(2022,10,4,2),[[11,27],[11,23]],"Test Fail")

    def test_DayLength_WhenUnsuccessful(self):
        self.assertNotEqual(getVariableDayLength(2022,10,4,1),[[11,23]],"Test Fail")
        self.assertNotEqual(getVariableDayLength(2022,10,4,1),[[11,28]],"Test Fail")


if __name__ == '__main__':
    unittest.main()