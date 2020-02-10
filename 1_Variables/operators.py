# Operators
# =, -, *, /, // (floor division)
# % (modulo): 'mod' remainder
# ** (power)

print(10 % 3)  # 1
print(10 ** 2)  # 100
print(100 // 3)  # 33
print(100 - 5)

# = : assignment
number = 7
number = number + 3  # increment number by 3
number += 3  # increment number by 3
# -= : decrement operator
print("number = " + str(number)) # string concatenation (+)

# *= : multiply by
number *= 2

# /= : divide by

# Boolean Operators
# Comparison
# == : equality (equal)
print(3 == 4)
# != :  not equal to
# > : greater than
# >= : greater than or equal to
# <= : less than or equal to
print(3 < 4)

x = 10
# check if x is greater than equal to 7 and less than 12
print(x >= 7 and x < 12)  # and (both have to be true to return TRUE), or (either one has to be true to return TRUE)

print(7 <= x < 12)  # only in python! same as "print(x >= 7 and x < 12)"
print((3 != 3) or (4 == 4))

# 4 == death (in chinnes), 13 == bad luck

# Exercise
num = 10
# print((num > 10) and (num / 0 = 0))  # ZeroDivisionError
print((num > 10) and (num / 0 == 0))  # False
print((num > 7) or (num / 0 == 0))  # True
# print((num > 10) or (num / 0 = 0))  # ZeroDivisionError
print(not True)  # False
print(not False)  # True
