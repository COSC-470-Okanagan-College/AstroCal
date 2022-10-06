import unittest

from AstroCal.control.control import getWhenSolEclipseLoc


class TestEclipse(unittest.TestCase):
    def test_SolEcl_WhenSuccessful(self):
        self.assertEqual(getWhenSolEclipseLoc(2022, 9, 27),
                         '2023-10-14 08:09:00-07:00', "Test Fail")

    def test_SolEcl_WhenUnsuccessful(self):
        self.assertNotEqual(getWhenSolEclipseLoc(
            2024, 9, 27), '2023-10-14 08:09:00-07:00', "Test Fail")
