import unittest
from io import StringIO
import sys
from unittest.mock import patch

class ISPPricesTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=["A", "15"])
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
        
        EXPECTED_PRICE = "19.95"

        # Assert the output is as expected
        self.assertIn(EXPECTED_PRICE, output)

    @patch('builtins.input',side_effect=["B", "25"])
    def test_package_b(self, mock_input):
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
        
        EXPECTED_PRICE = "18.95"

        # Assert the output is as expected
        self.assertIn(EXPECTED_PRICE, output)
       
    @patch('builtins.input',side_effect=["C", "90001"])
    def test_package_c(self, mock_input):
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
        
        EXPECTED_PRICE = "19.95"

        # Assert the output is as expected
        self.assertIn(EXPECTED_PRICE, output)
       
       

if __name__ == '__main__':
    unittest.main()