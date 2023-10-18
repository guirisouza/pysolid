from dip.refactored.email import Email
from dip.refactored.sms import Sms
from dip.refactored.mailer import Mailer


def main():
    mailer1 = Mailer(Email())
    mailer1.send_token()

    mailer2 = Mailer(Sms())
    mailer2.send_token()

if __name__ == '__main__':
    main()