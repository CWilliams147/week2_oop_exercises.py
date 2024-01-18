class Vehicle:
    def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year
    def print_info(self):
        print(f"({self.year}, {self.make}, {self.model})")

car1 = Vehicle( make = 'Lamborghini', model = 'Aventador', year = 2020)
car1.print_info()