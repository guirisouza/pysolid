from dip.unrefactored.message_interface import MessageInterface


class Sms(MessageInterface):
    def send(self):
        print('sms: seu token é 444')