# Data types
# There are many different data types in Python
# int: integer
# float: floating point (10.23, 3.14, etc)
# bool: boolean (True, False)
# str: a sequence of characters in quotes "aa", 'aa'

language = "en_us"
print(type(language))  # check the type of the variable

users = 10
"""
print(users + language)  # ERROR - we must match the type 
"""
print(str(users) + language)

# Type conversion (type changing): "changing types".
# There are several built-in functions that let you convert one data type to another.

# str(x): converts x into a string representation.
# int(x): converts x into an integer.
# float(x): converts x into a floating-point number.

#Ecercise: what is the type of following operations?
# 10. 1 / 2 -> float
print(str(1/2))
# 2. 10 //  4 -> int division
print(type(10 // 4))
# 3. float("a.12") -> Error
# 4. float(5) -> 5.0 (float)
print(float(5))