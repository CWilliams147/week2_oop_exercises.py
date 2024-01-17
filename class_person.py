print(" ")

class Person:
    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone

    def greet(self, other_person):
      print('Hello %s, I am %s!' % (other_person.name, self.name))
#here i am creating a profile for each of the characters
sonny = Person(name = 'Sonny', email = 'sonny@hotmail.com', phone = "483-485-4948")

jordan = Person(name = 'Jordan', email = 'jordan@aol.com', phone = '495-586-3456')
#this is calling the greet function for sonny using jordan as the other person
sonny.greet(jordan)

jordan.greet(sonny)
print("Contact info:")
print("-------------")
print("Sonny:", sonny.email,",", sonny.phone)
print("Jordan:", jordan.email,",", jordan.phone)
print(" ")
