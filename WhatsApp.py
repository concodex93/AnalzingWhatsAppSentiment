class WhatsApp:

    name = ""
    message = ""

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def get_name(self):
        return self.name

    def get_message(self):
        return self.message