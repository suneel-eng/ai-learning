# OOP helps you organize code into reusable, modular components.

# class - Blueprint for creating objects
# object - Instance of a class
# attribute - Variable inside a class
# method - Function defined inside a class
# inheritance - One class inherits from another
# encapsulation - Hides internal details
# polymorphism - Same method name, different behavior

# Creating a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Woof! my name is {self.name}")

# Creating an object
dog = Dog("Simba", "Golden Retriever")
dog.bark()

# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

# Cat inherits the Animal class
class Cat(Animal):
    # Polymorphism - Overriding the speak method
    def speak(self):
        print("Meow!")

kitty = Cat()
kitty.speak()

# Encapsulation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # Private attribute
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
# account.__balance  ❌ This will raise an error (encapsulated)
balance = account.get_balance()
print(balance)