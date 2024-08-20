'''

    @Author: Ayush Prajapati
    @Date: 19-08-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 20-09-2024 
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


def is_valid_last_name(last_name):
    """
    Description: 
        This function validates last name of the user
    Parameters:
        last_name : last name of the user
    Return:
        bool: Whether valid or not
    """
    ## Pattern: Last name starts with Cap and has minimum 3 characters
    last_name_pattern = r"^[A-Z][a-zA-Z]{2,}$"
    return bool(re.match(last_name_pattern, last_name))


def is_valid_email(email):
    """
    Description: 
        This function validates email of the user
    Parameters:
        email: email of the user
    Return:
        bool: Whether valid or not
    """
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_pattern, email))


def is_valid_phone_number(phone_number):
    """
    Description: 
        This function validates phone number of the user
    Parameters:
        phone_number: phone number of the user
    Return:
        bool: Whether valid or not
    """
    phone_number_pattern = r"^\d{2,3}\s\d{10}$"
    return bool(re.match(phone_number_pattern, phone_number))


def is_valid_password(password):
    """
    Description: 
        This function validates password of the user
    Parameters:
        password: password of the user
    Return:
        bool: Whether valid or not
    """
    password_pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
    return bool(re.match(password_pattern, password))


def main():
    print("*** Welcome to User Registration Validation System ***")
    logger = create_logger("user-registration")

    try:
        # for first name
        while True:
            first_name = input("\nEnter the first name of the user: ")
            if is_valid_first_name(first_name):
                logger.info(f"The user first name '{first_name}' is Valid")
                break
            else:
                logger.info(f"The user first name '{first_name}' is Not Valid. Please try again.")

        # for last name
        while True:
            last_name = input("\nEnter the last name of the user: ")
            if is_valid_last_name(last_name):
                logger.info(f"The user last name '{last_name}' is Valid")
                break
            else:
                logger.info(f"The user last name '{last_name}' is Not Valid. Please try again.")

        # for email
        while True:
            email = input("\nEnter the email of the user: ")
            if is_valid_email(email):
                logger.info(f"The user email '{email}' is Valid")
                break
            else:
                logger.info(f"The user email '{email}' is Not Valid. Please try again.")

        # for phone number
        while True:
            phone_number = input("\nEnter the phone number of the user: ")
            if is_valid_phone_number(phone_number):
                logger.info(f"The user phone number '{phone_number}' is Valid")
                break
            else:
                logger.info(f"The user phone number '{phone_number}' is Not Valid. Please try again.")

        # for password
        while True:
            password = input("\nEnter the password of the user: ")
            if is_valid_password(password):
                logger.info(f"The user password '{password}' is Valid")
                break
            else:
                logger.info(f"The user password '{password}' is Not Valid. Please try again.")


        print("\n\nThe user details are:")
        print(f"The First name is: {first_name}")
        print(f"The Last name is: {last_name}")
        print(f"The E-mail is: {email}")
        print(f"The Phone number is: {phone_number}")
        print(f"The Password is: {password}")
        print("\nThank you\nExiting.......")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
