# Indexing a list

countries = ["Brazil", "Japan", "Colombia", "Slovakia", "Mexico", "Canada", "USA", "Korea", "Iran"]

print(countries)
print(countries[-1])
print(countries[0])
print(len(countries[0]))

# Modify (change, mutate) elements (Lists are MUTABLE)
countries[-2] = "South Korea"
print(countries)

# Slicing lists (end index is not inclusive)
print(countries[0:3])  # 0 =<  < 3
countries[5:9] = []  # remove last four elements
print(countries)
countries[0:3] = ["UN"]  # replace 3 first items to "UN"
print(countries)
print(countries[:2])
print(countries[2:])
print(["2", "3"] * 5)

# String vs List
# list can contain different types
# list is mutable  list[0] = ...(0), you access and change
# string only contain chars
# string is immutable, you cannot change anything inside string


li =["String", 10, True, 3.14, [1, 2, 3]]
l = li[-1][0]  # access a list of lists
b = li[0]
print(b)
print(l)