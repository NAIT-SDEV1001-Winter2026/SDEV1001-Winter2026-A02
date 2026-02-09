import unittest
from io import StringIO
import sys
from unittest.mock import patch

class AverageAgeOfStudentsTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=['five', 'stop'])
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
        
        EXPECTED_INPUT_EXCEPTION = "Please enter a valid age"
        EXPECTED_ZERO_DIVISION_EXCEPTION = "You didn't enter any ages to average"
        # Assert the output is as expected
        self.assertIn(EXPECTED_INPUT_EXCEPTION, output)
        self.assertIn(EXPECTED_ZERO_DIVISION_EXCEPTION, output)
       

if __name__ == '__main__':
    unittest.main()