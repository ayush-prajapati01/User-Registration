'''

    @Author: Ayush Prajapati
    @Date: 19-08-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 19-09-2024 
    @Title: Python User Registration System that ensure all validations
            are in place during the User Entry
    
'''


import re
from logging_helper import create_logger


def is_valid_first_name(first_name):
    """
    Description: 
        This function validates first name of the user
    Parameters:
        first_name : first name of the user
    Return:
        bool: Whether valid or not
    """
    ## Pattern: First name starts with Cap and has minimum 3 characters
    first_name_pattern = r"^[A-Z][a-zA-Z]{2,}$"
    return bool(re.match(first_name_pattern, first_name))


def main():
    print("Welcome to User Registration Validation System")
    logger = create_logger("user-registration")

    try:
        first_name = input("Enter the first name of the user: ")

        if is_valid_first_name(first_name):
            logger.info(f"The user first name '{first_name}' is Valid")
        else:
            logger.info(f"The user first name '{first_name}' is Not Valid")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
