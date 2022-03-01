from helpers import calculateSum, Colors
from ast import arg


class Human:
    name = ''
    surname = ''

    def __init__(self, name, surname):
            self.name = name
            self.surname = surname
    
    def print(self):
        if self.name and self.surname:
            print(self.name + " " + self.surname)
        elif self.name:
            print(self.name)

class SuperHuman(Human):
    pass 
    superpower = ''
    livesSaved = 0

    def __init__(self, name, surname, superpower):
        super().__init__(name, surname)
        self.superpower = superpower

    def print(self):

        def innerPrint():
            global y
            y = 400
            print("My superpower is: " + self.superpower)
        
        super().print()
        innerPrint()


h1 = Human("marios", "kosmas")
h2 = SuperHuman("marianna", "lampou", "fly")


print(calculateSum([2,3,4,5]))




try:
  print(y)
except:
  print("y is not initialized yet")

h1.print()
h2.print()




print(Colors.values())