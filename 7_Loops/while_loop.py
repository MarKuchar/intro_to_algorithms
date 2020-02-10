# While-loop
# A while loop is similar to an if statement it executes some code while the given condition is true
# It will continue to execute the code for as long as the condition is True

# Syntax
# while __condition__:
#       code to repeat

num = 1
while num <= 10:
    print(num)
    num += 1

print("Done!")

# Exercise
# Print all squares from 1 to 99. (1, 4, 3, ..) using while-loop

num = 1
while num * num < 99:
    print(num * num)
    num += 1

print("Done!")


