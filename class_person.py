print(" ")

class Person:
    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone
      self.firends = []

    def greet(self, other_person):
      print('Hello %s, I am %s!' % (other_person.name, self.name))

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")


#here i am creating a profile for each of the characters
sonny = Person(name = 'Sonny', email = 'sonny@hotmail.com', phone = "483-485-4948")

jordan = Person(name = 'Jordan', email = 'jordan@aol.com', phone = '495-586-3456')
#this is calling the greet function for sonny using jordan as the other person

# Add friends
jordan.friends.append(sonny)
sonny.friends.append(jordan)

# Get the number of friends
num_friends_jordan = len(jordan.friends)
num_friends_sonny = len(sonny.friends)

print(f"{jordan.name} has {num_friends_jordan} friend(s).")  # Output: Jordan has 1 friend(s).
print(f"{sonny.name} has {num_friends_sonny} friend(s).")    # Output: Sonny has 1 friend(s).


sonny.greet(jordan)

jordan.greet(sonny)
print("Contact info:")
print("-------------")
print(" ")
print("Sonny's Contact Info:")
sonny.print_contact_info()
print(" ")
print("Jordan's Contact Info:")
jordan.print_contact_info()
print(" ")
