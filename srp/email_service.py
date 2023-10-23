

class EmailService:

    @classmethod
    def send(cls, to: str = "", subject: str = "", content: str = "", _from: str = "hi@app.com"):
        _from: str = _from
        to: str = to
        subject: str = subject
        content: str = content
        return f"sending email from {_from} to {to} - SUBJECT: {subject} | CONTENT: {content}"

