from typing import Union

from dip.unrefactored.email import Email
from dip.unrefactored.sms import Sms


class Mailer():
    def __init__(self):
        self.channel = None

    def get_channel(self):
        return self.channel

    def set_channel(self, chanel: str) -> None:
        self.channel = chanel

    def send_token(self) -> None:
        {
            "sms": Sms(),
            "email": Email()
        }.get(self.channel).send()

