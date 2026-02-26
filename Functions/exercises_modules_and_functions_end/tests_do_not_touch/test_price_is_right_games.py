import unittest

import os
import sys
import inspect
from unittest.mock import patch

# import the parent module as a workaround to import the module to test
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# import the module to test as if you were in the parent directory
from price_is_right_games import guess_items_price

class PIRGamesTestCase(unittest.TestCase):
    @patch('random.randint')
    def test_correct_guess(self, randint_mock):
        # simulate random
        randint_mock.side_effect = [1, 2, 3]

        # user guess
        USER_GUESS = 2
        # Get the value of the captured output
        value = guess_items_price(USER_GUESS)

        # Define the expected output in the test case        
        EXPECTED_RESULT = True

        # Assert the output is as expected
        self.assertEqual(EXPECTED_RESULT, value)

    @patch('random.randint')
    def test_not_correct_guess(self, randint_mock):
        # simulate random
        randint_mock.side_effect = [1, 2, 3]

        # user guess
        USER_GUESS = 9

        # Get the value of the captured output
        value = guess_items_price(USER_GUESS)

        # Define the expected output in the test case        
        EXPECTED_RESULT = False

        # Assert the output is as expected
        self.assertEqual(EXPECTED_RESULT, value)

if __name__ == '__main__':
    unittest.main()