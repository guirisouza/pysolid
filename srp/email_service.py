

class EmailService:
    def __init__(self, to: str = "", subject: str = "", content: str = "", _from: str = "hi@app.com"):
        self._from = _from
        self.eto = to
        self.subject = subject
        self.content = content

    def send(self):
        return "email sent"

