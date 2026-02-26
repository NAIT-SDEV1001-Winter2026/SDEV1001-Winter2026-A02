import unittest

import os
import sys
import inspect

# import the parent module as a workaround to import the module to test
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# import the module to test as if you were in the parent directory
from score_calculator import calculate_handicap, calculate_average


class ScoreCalculatorTestCase(unittest.TestCase):
    def test_average(self):
        # Simulate user input

        # Get the value of the captured output
        value = calculate_average(100, 90, 80, 90)

        # Define the expected output in the test case        
        EXPECTED_SCORE = 90

        # Assert the output is as expected
        self.assertEqual(EXPECTED_SCORE, value)

    def test_handicap_number(self):
        # Get the value of the captured output
        value = calculate_handicap(100, 90, 80, 90, 90, 600)

        # Define the expected output in the test case        
        EXPECTED_HANDICAP = 18

        # Assert the output is as expected
        self.assertEqual(EXPECTED_HANDICAP, value)

    def test_handicap_not_enough_numbers(self):
        # Get the value of the captured output
        value = calculate_handicap(100, 90, 80)

        # Define the expected output in the test case        
        NOT_EXPECTED_VALUE = 18

        # Assert the output is as expected
        self.assertNotEqual(NOT_EXPECTED_VALUE, value)


if __name__ == '__main__':
    unittest.main()