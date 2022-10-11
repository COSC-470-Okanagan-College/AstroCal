import unittest

from AstroCal.view.console_output import checkInputType, restrictInputToRangeInclusive


class TestSanitizeInputs(unittest.TestCase):
    def test_checkInputType_int_1(self):
        self.assertEqual(checkInputType("2", int), True, "Int 1 Failed")
        self.assertEqual(checkInputType("2.0", int), False, "Int 2 Failed")
        self.assertEqual(checkInputType(
            "words of wisdom", int), False, "Int 3 Failed")

    def test_checkInputType_float(self):
        self.assertEqual(checkInputType("2", float), True, "Float 1 Failed")
        self.assertEqual(checkInputType("2.0", float), True, "Float 2 Failed")
        self.assertEqual(checkInputType(
            "words of wisdom", int), False, "Float 3 Failed")

    def test_checkInputType_str(self):
        self.assertEqual(checkInputType("2", str), True, "Str 1 Failed")
        self.assertEqual(checkInputType("2.0", str), True, "Str 2 Failed")
        self.assertEqual(checkInputType(
            "words of wisdom", str), True, "Str 3 Failed")

    def test_restrictInputToRangeInclusive_whenSuccessful(self):
        self.assertEqual(restrictInputToRangeInclusive(
            0, 0, 100), True, "Inclusive min Failed")
        self.assertEqual(restrictInputToRangeInclusive(
            50, 0, 100), True, "In Range Failed")
        self.assertEqual(restrictInputToRangeInclusive(
            100, 0, 100), True, "inclusive max Failed")

    def test_restrictInputToRangeInclusive_whenUnsuccessful(self):
        self.assertEqual(restrictInputToRangeInclusive(-1,
                                                       0, 100), False, "Lower than min Failed")
        self.assertEqual(restrictInputToRangeInclusive(
            101, 0, 100), False, "Higher than max Failed")
