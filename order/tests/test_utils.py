import json
from django.test import TestCase
from rest_framework import status
from ..utils import SendSMs


class SendSMsTest(TestCase):

    def test_invalid_sender_id(self):
        """
        Test SMS cannot be sent with invalid sender ID
        :return: None
        """
        to_send = SendSMs('test message', ['+254728032118'], sender='CODE')
        response = to_send.send()
        self.assertEqual(response['SMSMessageData']['Message'], 'InvalidSenderId')

    def test_invalid_phone_number(self):
        """
        Test SMS cannot be sent with invalid phone_number
        :return: None
        """
        to_send = SendSMs('test message', ['+25472783201'])
        response = to_send.send()

        self.assertEqual(response['SMSMessageData']['Recipients'][0]['status'], 'InvalidPhoneNumber')
        self.assertEqual(response['SMSMessageData']['Recipients'][0]['statusCode'], status.HTTP_403_FORBIDDEN)

    def test_empty_message(self):
        """
        Test that an SMS cannot be sent with empty message
        :return: None
        """
        to_send = SendSMs('', ['+254727832012'])
        response = to_send.send()

        self.assertIsNone(response)

    def test_sms_can_be_sent(self):
        """
        Test that an SMS can be sent when correct credentials are provided
        :return: None
        """

        to_send = SendSMs('Hello test message', ['+254727832012'])
        response = to_send.send()

        self.assertEqual(response['SMSMessageData']['Recipients'][0]['status'], 'Success')
        self.assertEqual(response['SMSMessageData']['Recipients'][0]['statusCode'], status.HTTP_101_SWITCHING_PROTOCOLS)

