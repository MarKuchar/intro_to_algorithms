# Conditional statements
# (if-else statements)

# Getting user input
# input(prompt) - takes user input and returns as string

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # age = int(age)

if age >= 21:
    print("You can start drinking!")
elif 13 < age < 21:
    print("Study hard for SAT!")
else:
    print("Play video games!")

