import unittest
from io import StringIO
import sys
from unittest.mock import patch

class TechShowsTestCase(unittest.TestCase):
    def test_correct(self):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('tech_shows.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_FIRST = "Silicon Valley"
        EXPECTED_LAST = "Pirates of Silicon Valley"
        EXPECTED_FOURTH_TO_NINTH = "['The Billion Dollar Code', 'Mr. Robot', 'The IT Crowd', 'The Dropout', 'Black Mirror', 'Severance']"

        # Assert the output is as expected
        self.assertIn(EXPECTED_FIRST, output)
        self.assertIn(EXPECTED_LAST, output)
        self.assertIn(EXPECTED_FOURTH_TO_NINTH, output)

if __name__ == '__main__':
    unittest.main()