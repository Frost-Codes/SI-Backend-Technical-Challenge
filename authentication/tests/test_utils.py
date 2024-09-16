from django.test import TestCase
from ..utils import validate_number


class ValidateNumberTest(TestCase):
    def test_validate_number(self):
        """
        asserts functions validate_number works as expected
        :return:
        """

        # test phone number has len == 13
        status, message = validate_number('+25477322018')
        self.assertFalse(status, msg='Phone number status validation failed, Phone number too short, min len is 13')
        self.assertEqual(message, 'Invalid Phone Number',
                         msg='Phone number message validation failed phone number too short, min len is 13')

        status, message = validate_number('+2547227322018')
        self.assertFalse(status, msg='Phone number status validation failed, Phone number too long, max len is 13 ')
        self.assertEqual(message, 'Invalid Phone Number',
                         msg='Phone number message validation failed phone number too long, max len is 13')

        # test phone number begins with +254
        status, message = validate_number('+255727322018')
        self.assertFalse(status, msg='Phone number status validation failed, Incorrect country code')
        self.assertEqual(message, 'Invalid Phone Number',
                         msg='Phone number message validation failed Incorrect country code')

        # test phone number has digits 1-9 after country code
        status, message = validate_number('+255027322018')
        self.assertFalse(status, msg='Phone number status validation failed, Invalid number after country code')
        self.assertEqual(message, 'Invalid Phone Number',
                         msg='Phone number message validation failed, Invalid number after country code')

        # sample correct kenyan phone number
        status, message = validate_number('+254727322018')
        self.assertTrue(status, msg='Phone number status validation failed')
        self.assertEqual(message, 'Valid Phone Number', msg='Phone number message validation failed')
