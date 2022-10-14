import unittest
from unittest.mock import patch
from AstroCal.view.console_output import checkInputType, restrictInputToRangeInclusive, getInputSanitized


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

    @patch('AstroCal.view.console_output.getInput', return_value='2')
    def test_getInput_rawInput_int(self, return_value):
        self.assertEqual(getInputSanitized(), '2', "Test Failed")

    @patch('AstroCal.view.console_output.getInput', return_value='2')
    def test_getInput_correctType_int_success(self, return_value):
        self.assertEqual(getInputSanitized(None, None, int), 2, "Test Failed")

    @patch('AstroCal.view.console_output.getInput', return_value='2')
    def test_getInput_correctType_int_failed(self, return_value):
        self.assertNotEqual(getInputSanitized(
            None, None, None), 2, "Test Failed")

    @patch('AstroCal.view.console_output.getInput', return_value='2')
    def test_getInput_noInput_noDefault(self, return_value):
        self.assertNotEqual(getInputSanitized(
            None, None, None), '', "Test Failed")

    @patch('AstroCal.view.console_output.getInput', return_value='')
    def test_getInput_noInput_withDefault(self, return_value):
        self.assertEqual(getInputSanitized(
            None, None, None, None, None, "Testing"), 'Testing', "Test Failed")

    @patch('AstroCal.view.console_output.getInput', return_value='2')
    def test_getInput_withInput_withDefault(self, return_value):
        self.assertEqual(getInputSanitized(
            None, None, None, None, None, "Testing"), '2', "Test Failed")

    @patch('AstroCal.view.console_output.getInput', return_value='2')
    def test_getInput_withRange_inRange(self, return_value):
        self.assertEqual(getInputSanitized(
            None, None, int, 0, 20), 2, "Test Failed")
