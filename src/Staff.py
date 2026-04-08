from src.Person import Person
class Staff(Person):
    def __init__(self, id, name, email, subject):
        super().__init__(id, name, email)
        self.subject = subject

    def display_info(self):
        print(self.name, self.email, self.subject)

    def __str__(self):
        return f"Staff(ID: {self.id}, Name: {self.name}, Username: {self.email}, Subject: {self.subject})"