import unittest
from io import StringIO
import sys
from unittest.mock import patch

class VisitableInterestingCitiesTestCase(unittest.TestCase):
    @patch('builtins.input',return_value='Edmonton')
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
        
        EXPECTED_LIST = "Amsterdam is an interesting city that we can visit\nEdmonton is an interesting city that we can visit\nParis is an interesting city that we can visit\nPrague is an interesting city that we can visit"
        self.assertIn(EXPECTED_LIST.lower(), output.lower())
       

if __name__ == '__main__':
    unittest.main()