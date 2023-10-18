from dip.unrefactored.mailer import Mailer


def main():
    mailer1 = Mailer()
    mailer1.set_channel(chanel='email')
    mailer1.send_token()

    mailer2 = Mailer()
    mailer2.set_channel(chanel='sms')
    mailer2.send_token()

if __name__ == '__main__':
    main()