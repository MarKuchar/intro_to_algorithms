# Data structure
# list: A sequence of items (elements)

# 1. How to create a list
squares = [1, 2, 9, 16, 25, 36, 49]
print(squares)

# 2. How we operate a list
squares += [64, 81]  # add two elements at the end of the list
print(squares)

# 3. List methods
animals = ["Eagle", "Beaver", "Jaguar", "Rooster", "Monkey", "Panda", "Condor"]
animals.append("Dog")  # will add "Dog" to the end of the list
print(animals)

animals.insert(0, "Cat")  # insert "Cat" at 0 index
print(animals)

animals.remove("Rooster")  # remove "Rooster" from list
print(animals)

animals.pop(0)  # remove element at index 0
print(animals)

animals.count("Beaver")  # will give us integer
print(animals)

animals.index("Panda")  # will give us index of "Panda" it always starts from 0
print(animals)

# 4.