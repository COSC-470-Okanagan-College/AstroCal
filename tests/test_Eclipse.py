import unittest

from AstroCal.control.control import getWhenSolEclipseLoc


class TestEclipse(unittest.TestCase):
    def test_SolEcl_WhenSuccessful(self):
        self.assertEqual(getWhenSolEclipseLoc(2022, 9, 27),
                         (2023, 10, 14, 15, 9, 15.699218809604645), "Test Fail")

    def test_SolEcl_WhenUnsuccessful(self):
        self.assertNotEqual(getWhenSolEclipseLoc(
            2022, 9, 27), (2024, 10, 14, 15, 9, 15.699218809604645), "Test Fail")
