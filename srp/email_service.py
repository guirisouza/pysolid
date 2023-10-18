

class EmailService:
    def __init__(self, eto: str = "", subject: str = "", content: str = "", efrom: str = "hi@app.com"):
        self.efrom = efrom
        self.eto = eto
        self.subject = subject
        self.content = content

    def send(self):
        return "email enviado"

