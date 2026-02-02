import unittest
from io import StringIO
import sys
from unittest.mock import patch

class InterestingCitiesTestCase(unittest.TestCase):
    @patch('builtins.input',return_value='London')
    def test_correct(self, mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('interesting_cities.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_CITIES = "['Amsterdam', 'Berlin', 'London', 'Munich', 'Paris', 'Prague']"
        

        # Assert the output is as expected
        self.assertIn(EXPECTED_CITIES, output)
       

if __name__ == '__main__':
    unittest.main()