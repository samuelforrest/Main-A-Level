import random

class Dog:  #This is type Dog
  name = ""
  age = random.randint(1,160)

  def __init__(self, aName, age):
    self.name = aName
    self.age = a

  def __str__(self):
    return "Woof!"

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

  def haveBirthday(self):
    return self.haveBirthday
    age += random.randint(1,30)
    
rover = Dog("Rover")
patch = Dog("Patch")
rufus = Dog("Rufus")
archie = Dog("Archie")
rory = Dog("Rory")

class StBernard(Dog):
  rescued = 0

  def __init__(self, aName, rescued, age):
    self.rescued=rescued
    Dog.__init__(self, aName)

  def getRescued(self):
      return self.rescued

if rover.age > 100:
  print("Rover is about to die!")
  
print(rover, rover)
print(rover.name, "is",rover.age, "Years old today!")
print(rover)