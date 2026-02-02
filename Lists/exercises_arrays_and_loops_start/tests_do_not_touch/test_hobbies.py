import unittest
from io import StringIO
import sys
from unittest.mock import patch

class HobbiesTestCase(unittest.TestCase):
    def test_correct(self):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('hobbies.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_LENGTH = "9"
        EXPECTED_FIFTH_ITEM = "playing golf"
        EXPECTED_FIRST_FOUR_ITEMS = "['playing squash', 'programming', 'reading', 'petting cats']"
        EXPECTED_LAST_THREE_ITEMS = "['playing video games', 'playing board games', 'watching movies']"

        # Assert the output is as expected
        self.assertIn(EXPECTED_LENGTH, output)
        self.assertIn(EXPECTED_FIFTH_ITEM, output)
        self.assertIn(EXPECTED_FIRST_FOUR_ITEMS, output)
        self.assertIn(EXPECTED_LAST_THREE_ITEMS, output)

if __name__ == '__main__':
    unittest.main()