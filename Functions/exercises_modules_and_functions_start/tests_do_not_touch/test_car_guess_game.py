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
from price_is_right_games import guess_car_price

class CarPriceTestCase(unittest.TestCase):
    @patch('random.randint', return_value=25000)
    def test_correct_guess(self, randint_mock):

        # user guess
        USER_GUESS = 25000
        # Get the value of the captured output
        value = guess_car_price(USER_GUESS)

        # Define the expected output in the test case        
        EXPECTED_RESULT = "You win! That's exactly the price! You're a cheater!"

        # Assert the output is as expected
        self.assertEqual(EXPECTED_RESULT, value)
    
    @patch('random.randint', return_value=25000)
    def test_winning_guess(self, randint_mock):

        # user guess
        USER_GUESS = 24500
        # Get the value of the captured output
        value = guess_car_price(USER_GUESS)

        # Define the expected output in the test case        
        EXPECTED_RESULT = "You win!"

        # Assert the output is as expected
        self.assertEqual(EXPECTED_RESULT, value)

    @patch('random.randint', return_value=25000)
    def test_close_guess(self, randint_mock):

        # user guess
        USER_GUESS = 22500
        # Get the value of the captured output
        value = guess_car_price(USER_GUESS)

        # Define the expected output in the test case        
        EXPECTED_RESULT = "You're close!"

        # Assert the output is as expected
        self.assertEqual(EXPECTED_RESULT, value)


    @patch('random.randint', return_value=25000)
    def test_bad_guess(self, randint_mock):

        # user guess
        USER_GUESS = 10000
        # Get the value of the captured output
        value = guess_car_price(USER_GUESS)

        # Define the expected output in the test case        
        EXPECTED_RESULT = "Sorry you lose!"

        # Assert the output is as expected
        self.assertEqual(EXPECTED_RESULT, value)

if __name__ == '__main__':
    unittest.main()