import unittest
from datetime import datetime
from AstroCal import control


class TestControlTest(unittest.TestCase):
    # Test Cases
    # Happy path
    # Null cases (input null)
    # input badly formatted data
    def test_sun(self):
        some_time = datetime(2022, 9, 5)
        output = control.getRiseSet(some_time.year, some_time.month,
                                    some_time.day, 'SUN', 'RISE')
        # print(output)
        self.assertTrue(True)
        self.assertEqual(output, "07:19")


if __name__ == '__main__':
    unittest.main()