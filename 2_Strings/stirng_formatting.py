# Escape characters
# - newline: "\n"
# - tab: "\t"
# - quotes: \"

city = "va\nc\"ou\tver"
print(city)

dont_worry = "Do not worry about the \"weather\""
print(dont_worry)

message = "Ahoj \n ako sa mas \n ja som ok"
print(message)

phrase = """
Ahoj,
ako sa mas?
ja som OK!
"""
print(phrase)

# String formatting
# formatting chars
# %s: represent string
# %d: decimal (integer)
# %f: float

name = "Martin"
city = "Vancouver"
temp = 8
message1 = "Hello %s! My name is %s. The temp is %f." % (city, name, temp)
print(message1)

country = "Canada"
message2 = f"{country} is big"  # f is for formatting, I am gonna put a variable in! (string interpolation)
print(message2)

average_point = 80.43242
# 80.4
# {variable:{width_result}.{width_precision}}
print(f"The average point is {average_point}")
print(f"The average point is {average_point:{10}.{3}}")  #      80.432

print("The average point is %.2f" % average_point)

x = 10
y = 17
print(f"{x} x {y} = {x * y}")