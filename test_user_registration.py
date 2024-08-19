'''

    @Author: Ayush Prajapati
    @Date: 19-08-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 19-09-2024 
    @Title: Python Program to perform unit test on user_registration.py
    
'''


import unittest
from user_registration import is_valid_first_name


class TestUserRegistration(unittest.TestCase):

    def test_is_valid_first_name(self):
        # Unit test for `is_valid_first_name()` function
        self.assertTrue(is_valid_first_name('Ayush'))
        self.assertTrue(is_valid_first_name('Ayu'))
        self.assertFalse(is_valid_first_name('ayush'))
        self.assertFalse(is_valid_first_name('Ayush123'))


if __name__ == "__main__":
    unittest.main()