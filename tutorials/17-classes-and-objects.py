# Create a class
class MyClass:
    index = 1
    title = "Python"
    data = "tutorial"
    date = "today"

# Create an object
obj1 = MyClass()
print(obj1.index)

# Class with assignable values
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Animal('Charile', 2)
print(dog1.name)
print(dog1.age)

# Class with own method
class Animal:
    def __init__(this, name, age):
        this.name = name
        this.age = age

    def isAnimalHere(this):
        print("There is dog " + this.name)

dog2 = Animal("Charlie", 3)
dog2.isAnimalHere()

# Modify object
dog2.age = 4

# Delete object properties
del dog2.age

# Delete object
del dog1