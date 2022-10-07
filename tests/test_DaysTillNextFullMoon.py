import unittest

from AstroCal.control.control import getDaysTillFullMoon


class TestDaysTillFullMoon(unittest.TestCase):
    def test_DaysTillFullMoon_WhenSuccessful(self):
        self.assertEqual(getDaysTillFullMoon(2025, 6, 1, -7), 10, "Test Fail")

    def test_DaysTillFullMoon_WhenUnsuccessful(self):
        self.assertNotEqual(getDaysTillFullMoon(
            2025, 9, 25, -7), (12), "Test Fail")
