import os
import threading
import africastalking

africastalking_username = os.environ.get('africastalking_username')
africastalking_api_key = os.environ.get('africastalking_api_key')

africastalking.initialize(africastalking_username, africastalking_api_key)


class SMSThread(threading.Thread):
    def __init__(self, sms):
        super().__init__()
        self.sms = sms

    def run(self) -> None:
        self.sms.send()


class SendSMs:
    def __init__(self, message: str, recipients: list, sender: str = os.environ.get('sender')):
        self.sms = africastalking.SMS
        self.message = message
        self.recipients = recipients
        self.sender = sender

    def send(self):
        """
        Sends Message to customer
        :return: africastalking SMSMessage data if successful else None
        """
        try:
            response = self.sms.send(self.message, self.recipients, self.sender)
            if isinstance(response, dict):
                return response
            return response.__dict__

        except Exception as e:
            print(e)


# to_send = SendSMs("Hello from API", ["+254727832018"], 'CODEBLOCK')
# print(type(to_send))
# res = to_send.send()
# print(type(res))
# print(res)

# sms = SendSMs("Hello from API", ["+254727832018"], 'CODEBLOCK')
# SMSThread(sms=sms).start()