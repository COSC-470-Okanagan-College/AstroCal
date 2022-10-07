from datetime import datetime
import unittest

from AstroCal.control.control import getWhenSolEclipseLoc


class TestEclipse(unittest.TestCase):
    def test_SolEcl_WhenSuccessful(self):
        sol_eclipse_date_time = getWhenSolEclipseLoc(2022, 9, 27)
        self.assertEqual(sol_eclipse_date_time.year, 2023, "Year Test Fail")
        self.assertEqual(sol_eclipse_date_time.month, 10, "Month Test Fail")
        self.assertEqual(sol_eclipse_date_time.day, 14, "Day Test Fail")

    def test_SolEcl_WhenUnsuccessful(self):
        sol_eclipse_date_time = getWhenSolEclipseLoc(2024, 9, 27)
        self.assertNotEqual(sol_eclipse_date_time.year, 2023, "Year Test Fail")
        self.assertNotEqual(sol_eclipse_date_time.month, 10, "Month Test Fail")
        self.assertNotEqual(sol_eclipse_date_time.day, 14, "Day Test Fail")
