class Animal:
    def __init__(this, name, age):
        this.name = name
        this.age = age

    def isAnimalHere(this):
        print("There is dog " + this.name)


# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the chuld class
# Use the pass keyword when you do not want to add any other properties or methods to the class
class Dog(Animal):
    pass


# To create class that keeps the inheritance of the parent class
class Dog(Animal):
    def __init__(this, name, age, breed):
        Animal.__init__(this, name, age)
        this.breed = breed

dog1 = Dog("Charlie", 3, "Shepherd")
print(dog1.name)
print(dog1.age)
print(dog1.breed)