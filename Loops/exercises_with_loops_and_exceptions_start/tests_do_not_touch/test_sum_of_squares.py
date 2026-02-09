import unittest
from io import StringIO
import sys
from unittest.mock import patch

class SumOfSquaresTestCase(unittest.TestCase):
    @patch('builtins.input',return_value='4')
    def test_correct(self, mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('sum_of_squares.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_SUM_OF_SQUARES = "30"
        

        # Assert the output is as expected
        self.assertIn(EXPECTED_SUM_OF_SQUARES, output)
       

if __name__ == '__main__':
    unittest.main()