from typing import Union

from dip.unrefactored.email import Email
from dip.unrefactored.sms import Sms
from message_interface import MessageInterface


class Mailer():
    def __init__(self, chanel: MessageInterface):
        self.channel = chanel

    def get_channel(self) -> MessageInterface:
        return self.channel

    def send_token(self) -> None:
        self.get_channel().send()

