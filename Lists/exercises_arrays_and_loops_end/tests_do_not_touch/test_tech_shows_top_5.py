import unittest
from io import StringIO
import sys
from unittest.mock import patch

class TechShowsTopFiveTestCase(unittest.TestCase):
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
        
        EXPECTED_TOP_FIVE = "Ranked 1 is: Silicon Valley\nRanked 2 is: Halt and Catch Fire\nRanked 3 is: Blackberry\nRanked 4 is: The Billion Dollar Code\nRanked 5 is: Mr. Robot"
        

        # Assert the output is as expected
        self.assertIn(EXPECTED_TOP_FIVE, output)


if __name__ == '__main__':
    unittest.main()