from datetime import datetime, timedelta
import unittest
from AstroCal.control.control import getWhenSolEclipse, getWhenLunEclipse


class TestEclipse(unittest.TestCase):
    def test_SolEcl_WhenSuccessful(self):
        sol_eclipse_date_time_start, sol_eclipse_date_time_max, sol_eclipse_date_time_end, sol_eclipse_date_time_duration = getWhenSolEclipse(
            2022, 9, 27)
        self.assertEqual(sol_eclipse_date_time_start.year,
                         2022, "Year Test Fail")
        self.assertEqual(sol_eclipse_date_time_start.month,
                         10, "Month Test Fail")
        self.assertEqual(sol_eclipse_date_time_start.day,
                         25, "Day Test Fail")
        self.assertEqual(sol_eclipse_date_time_start.hour,
                         1, "Hour Start Test Fail")
        self.assertEqual(sol_eclipse_date_time_start.minute,
                         58, "Minute Start Test Fail")

        self.assertEqual(sol_eclipse_date_time_max.hour,
                         4, "Hour Max Test Fail")
        self.assertEqual(sol_eclipse_date_time_max.minute,
                         0, "Minute Max Test Fail")

        self.assertEqual(sol_eclipse_date_time_end.hour,
                         6, "Hour End Test Fail")
        self.assertEqual(sol_eclipse_date_time_end.minute,
                         2, "Minute End Test Fail")

        self.assertEqual(sol_eclipse_date_time_duration,
                         timedelta(hours=4, minutes=4), "Duration Test Fail")

    def test_SolEcl_WhenUnsuccessful(self):
        sol_eclipse_date_time_start, sol_eclipse_date_time_max, sol_eclipse_date_time_end, sol_eclipse_date_time_duration = getWhenSolEclipse(
            2024, 9, 27)
        self.assertNotEqual(sol_eclipse_date_time_start.year,
                            2023, "Year Test Fail")
        self.assertNotEqual(sol_eclipse_date_time_start.month,
                            4, "Month Test Fail")
        self.assertNotEqual(sol_eclipse_date_time_start.day,
                            20, "Day Test Fail")
        self.assertNotEqual(sol_eclipse_date_time_start.hour,
                            1, "Hour Start Test Fail")
        self.assertNotEqual(sol_eclipse_date_time_start.minute,
                            34, "Minute Start Test Fail")

        self.assertNotEqual(sol_eclipse_date_time_max.hour,
                            10, "Hour Max Test Fail")
        self.assertNotEqual(sol_eclipse_date_time_max.minute,
                            22, "Minute Max Test Fail")

        self.assertNotEqual(sol_eclipse_date_time_end.hour,
                            10, "Hour End Test Fail")
        self.assertNotEqual(sol_eclipse_date_time_end.minute,
                            41, "Minute End Test Fail")

        self.assertNotEqual(sol_eclipse_date_time_duration,
                            timedelta(hours=2, minutes=20), "Duration Test Fail")

    def test_LunEcl_WhenSuccessful(self):
        lun_eclipse_date_time_start, lun_eclipse_date_time_max, lun_eclipse_date_time_end, lun_eclipse_date_time_duration = getWhenLunEclipse(
            2022, 9, 27)
        self.assertEqual(lun_eclipse_date_time_start.year,
                         2022, "Year Test Fail")
        self.assertEqual(lun_eclipse_date_time_start.month,
                         11, "Month Test Fail")
        self.assertEqual(lun_eclipse_date_time_start.day,
                         8, "Day Test Fail")
        self.assertEqual(lun_eclipse_date_time_start.hour,
                         0, "Hour Start Test Fail")
        self.assertEqual(lun_eclipse_date_time_start.minute,
                         2, "Minute Start Test Fail")

        self.assertEqual(lun_eclipse_date_time_max.hour,
                         2, "Hour Max Test Fail")
        self.assertEqual(lun_eclipse_date_time_max.minute,
                         59, "Minute Max Test Fail")

        self.assertEqual(lun_eclipse_date_time_end.hour,
                         5, "Hour End Test Fail")
        self.assertEqual(lun_eclipse_date_time_end.minute,
                         56, "Minute End Test Fail")

        self.assertEqual(lun_eclipse_date_time_duration,
                         timedelta(hours=5, minutes=54), "Duration Test Fail")

    def test_LunEcl_WhenUnsuccessful(self):
        lun_eclipse_date_time_start, lun_eclipse_date_time_max, lun_eclipse_date_time_end, lun_eclipse_date_time_duration = getWhenLunEclipse(
            2024, 9, 27)
        self.assertNotEqual(lun_eclipse_date_time_start.year,
                            2024, "Year Test Fail")
        self.assertNotEqual(lun_eclipse_date_time_start.month,
                            4, "Month Test Fail")
        self.assertNotEqual(lun_eclipse_date_time_start.day,
                            4, "Day Test Fail")
        self.assertNotEqual(lun_eclipse_date_time_start.hour,
                            7, "Hour Start Test Fail")
        self.assertNotEqual(lun_eclipse_date_time_start.minute,
                            30, "Minute Start Test Fail")

        self.assertNotEqual(lun_eclipse_date_time_max.hour,
                            10, "Hour Max Test Fail")
        self.assertNotEqual(lun_eclipse_date_time_max.minute,
                            22, "Minute Max Test Fail")

        self.assertNotEqual(lun_eclipse_date_time_end.hour,
                            10, "Hour End Test Fail")
        self.assertNotEqual(lun_eclipse_date_time_end.minute,
                            41, "Minute End Test Fail")

        self.assertNotEqual(lun_eclipse_date_time_duration,
                            timedelta(hours=2, minutes=20), "Duration Test Fail")
