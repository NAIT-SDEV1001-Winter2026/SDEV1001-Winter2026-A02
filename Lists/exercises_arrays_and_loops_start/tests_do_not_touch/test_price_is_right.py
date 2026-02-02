import unittest
from io import StringIO
import sys
from unittest.mock import patch

class PriceIsRightTestCase(unittest.TestCase):
    @patch('random.randint',return_value=5)
    @patch('builtins.input',return_value='5')
    def test_correct(self, mock_input, mock_randint):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('price_is_right.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_OUTPUT = "You win!"
        

        # Assert the output is as expected
        self.assertIn(EXPECTED_OUTPUT, output)
       
    @patch('random.randint',return_value=10)
    @patch('builtins.input',return_value='5')
    def test_fail(self, mock_input, mock_randint):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('price_is_right.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_OUTPUT = "You lose!"
        

        # Assert the output is as expected
        self.assertIn(EXPECTED_OUTPUT, output)
if __name__ == '__main__':
    unittest.main()