import unittest

import os
import sys
import inspect

# import the parent module as a workaround to import the module to test
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# import the module to test as if you were in the parent directory
from squares_calculator import calculate_sum_of_squares

class SumOfSquaresTestCase(unittest.TestCase):
    def test_correct_for_four(self):
        # Simulate user input

        # Get the value of the captured output
        value = calculate_sum_of_squares(4)

        # Define the expected output in the test case        
        EXPECTED_SUM_OF_SQUARES = 30

        # Assert the output is as expected
        self.assertEqual(EXPECTED_SUM_OF_SQUARES, value)

    def test_correct_for_seven(self):
        # second test
        second_value = calculate_sum_of_squares(7)
        SECOND_EXPECTED_SUM_OF_SQUARES = 140
        
        # Assert the output is as expected
        self.assertEqual(SECOND_EXPECTED_SUM_OF_SQUARES, second_value)
       

if __name__ == '__main__':
    unittest.main()