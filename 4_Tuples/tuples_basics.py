# Tuples are almost identical to lists
# The only big difference between lists and tuples is that tuples cannot be modified (Immutable)
# You can NOT add(append), changed(replace), or delete "IMMUTABLE LIST"
# elements from the tuple

vowels = ("a", "e", "i", "o", "u")  # consonants (b, c, d, ...)
print(vowels[0])
print("k" in vowels)
# vowels[0] = "A"  # Error

# Methods
vowels.index("e")
vowels.count("i")

# Use cases
# 1. return multiple values from a function

def a():
    return (1, "Mars")

# example
def get_combo(name):
    if name == "Big-mac":
        return ("Coke", "Big-mac", "Fries")

# 2. check if an item is in a tuple

print("a" in vowels)

# 3. multiple assignments
year, country = (2020, "Canada")
_, country, provice = (2020, "Canada", "BC")  # underscore we use when we want to ignore part of assignment

# swap
x = 10
y = 20
# I want to swap x and y
# in python
x, y = y, x

# in other languages
temp = x  # temporary variable
x = y
y = temp

