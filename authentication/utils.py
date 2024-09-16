import re


def validate_number(number):
    """
    Checks whether a given number is a valid kenyan phone number
    :param number: phone_number
    :return: True and success message if valid else False and error message
    """
    phone_regex = re.compile(r'^\+254[1-9]\d{8}$')
    if not phone_regex.match(number):
        return False, "Invalid Phone Number"
    return True, "Valid Phone Number"



