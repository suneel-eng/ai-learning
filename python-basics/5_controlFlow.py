# Control flow lets your program react to data and automate repetitive tasks

# if, elif, else
temperature = 28

if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a warm day")
else:
    print("It's a cool day")

# for loop
for i in range(5):
    print("Iteration: ", i)

# while loop
count = 0
while count < 3:
    print("Count: ", count)
    count += 1

# Looping through lists
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello, ", name)

# Breaking & Skipping
for i in range(5):
    if i == 3:
        break  # stop the loop
    if i == 1:
        continue  # skip this iteration
    print(i)
