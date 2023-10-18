from dip.unrefactored.message_interface import MessageInterface


class Email(MessageInterface):
    def send(self):
        print('email: seu token é 444')