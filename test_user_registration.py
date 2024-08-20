'''

    @Author: Ayush Prajapati
    @Date: 19-08-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 20-09-2024 
    @Title: Python Program to perform unit test on user_registration.py
    
'''


import unittest
from user_registration import (
    is_valid_first_name, is_valid_last_name, is_valid_email,
    is_valid_phone_number, is_valid_password
) 


class TestUserRegistration(unittest.TestCase):

    def test_is_valid_first_name(self):
        # Unit test for `is_valid_first_name()` function
        self.assertTrue(is_valid_first_name('Ayush'))
        self.assertTrue(is_valid_first_name('Ayu'))
        self.assertFalse(is_valid_first_name('ayush'))
        self.assertFalse(is_valid_first_name('Ayush123'))
    
    
    def test_is_valid_last_name(self):
        # Unit test for `is_valid_first_name()` function
        self.assertTrue(is_valid_last_name('Prajapati'))
        self.assertTrue(is_valid_last_name('Pra'))
        self.assertFalse(is_valid_last_name('prajapati'))
        self.assertFalse(is_valid_last_name('pra'))
    

    def test_is_valid_email(self):
        # Unit test for `is_valid_email()` function
        self.assertTrue(is_valid_email('abc.xyz@bl.co.in'))
        self.assertTrue(is_valid_email('abc.xyz@bl.co.in'))
        self.assertFalse(is_valid_email('abc.xyz@bl'))
        self.assertFalse(is_valid_email('abc.xyz@bl.c'))
    

    def test_is_valid_phone_number(self):
        # Unit test for `is_valid_phone_number()` function"
        self.assertTrue(is_valid_phone_number('91 9919819801'))   
        self.assertTrue(is_valid_phone_number('123 9919819801'))  
        self.assertFalse(is_valid_phone_number('9 9919819801'))   
        self.assertFalse(is_valid_phone_number('1234 9919819801'))  
        self.assertFalse(is_valid_phone_number('91-9919819801'))  


    def test_is_valid_password(self):
        # Unit test for `is_valid_password()` function"
        self.assertTrue(is_valid_password('abcd1234'))
        self.assertFalse(is_valid_password('abcde'))


if __name__ == "__main__":
    unittest.main()