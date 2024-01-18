class Person:
    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone
#using f string interpilation is a lot simpler!
    def greet(self, other_person):
        print('Hello {}, I am {}!' .format(other_person.name, self.name))

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# call greet function while first calling the person
# Person.greet(sonny, jordan)
jordan.greet(sonny)
sonny.greet(jordan)
Person.print_contact_info(sonny)