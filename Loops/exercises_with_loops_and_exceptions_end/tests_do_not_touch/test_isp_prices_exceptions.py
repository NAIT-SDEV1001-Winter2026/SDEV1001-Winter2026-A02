import unittest
from io import StringIO
import sys
from unittest.mock import patch

class ISPPricesTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=["A", "filet mignon"])
    def test_package_a(self, mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('isp_prices.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_EXCEPTION = "Please enter a valid number of hours"

        # Assert the output is as expected
        self.assertIn(EXPECTED_EXCEPTION, output)

if __name__ == '__main__':
    unittest.main()