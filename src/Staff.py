from src.Person import Person
class Staff(Person):
    def __init__(self, ID, name, email, subject):
        Person.__init__(self, ID, name, email)
        self.subject = subject

    def display_info(self):
        print(self.name, self.email, self.subject)