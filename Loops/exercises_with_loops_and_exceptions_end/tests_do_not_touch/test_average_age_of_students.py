import unittest
from io import StringIO
import sys
from unittest.mock import patch

class AverageAgeOfStudentsTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=['10', '12', '14', '20', 'stop'])
    def test_correct(self, mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('average_age_of_students.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_AVERAGE_AGE = "14.0"

        # Assert the output is as expected
        self.assertIn(EXPECTED_AVERAGE_AGE, output)
       

if __name__ == '__main__':
    unittest.main()