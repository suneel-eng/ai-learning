# Reading a file
with open('read.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('write.txt', 'w') as file:
    file.write('Hello, dude!\n')
    file.write('You are learning AI like a pro!\n')

# Appending to a file
with open('write.txt', 'a') as file:
    file.write('This is an additional line.\n')

# Read a file line by line
with open('read.txt', 'r') as file:
    for line in file:
        print(line.strip()) # removes newline characters
