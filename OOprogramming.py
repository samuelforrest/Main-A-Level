class Human:
    
    def __init__(self, age, height, eyeColour, hairColour):
        self.age = age
        self.height = height
        self.eyeColour = eyeColour
        self.hairColour = hairColour

    def display_info(self):  # Make sure the method name is correct (case-sensitive) 
        
        return f"Age: {self.age}, Height: {self.height}, Eye Colour: {self.eyeColour}, Hair Colour: {self.hairColour}"

# Instantiate the object outside the class
myHuman = Human(16, 1.78, "blue", "brown")

myHuman2 = Human(18, 1.88, "blue", "blonde")

# Call the method on the object
print(myHuman.display_info())  # Method name should be `display_info` with all lowercase letters

print()
print("This is my ambitious human target:", myHuman2.display_info())
