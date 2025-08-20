# Lists - Ordered, mutable lists
fruits = ["apple", "banana", "grapes"]
print(fruits[0]) # Accessing first element

fruits.append("mango") # Add new element at the end
print(fruits)

print(fruits[-1]) # Accessing last element

print(len(fruits)) # Length of the list

# Iterate over list
for fruit in fruits:
    print(fruit)

# Lists can hold mixed values
mixed = [1, "apple", 3.14, True]
print(mixed)