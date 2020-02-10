# String (str) : A sequence of characters "" or ''
# + Concatenation : combining two strings
print("hello " + "world")

# * multiplication : repeat strings
print("hello" * 5)
# String indexing (index == position)
singer = "Lady Gaga"
# index 0123456789
# index always starts from "0"
print(singer[0])  # "L"
print(singer[7])  # "g"
print(singer[-1])  # last char "a"
# print(singer[-15])  # out of bounds "Error"

# String slicing (Substring)
# start_index <=  < end_string
actor = "Will Smith"
# index 0123456789
print(actor[0:4])  # "Will"
print(actor[2:6])  # "ll s"
print(actor[-3:-1])

# shortcuts
# starting at 0
print(actor[:4])

# go to the end from 5
print(actor[5:])

# from 0 to end
print(actor[:])

# How to get the number of characters? "len()"
print(len(actor))  # 10
# 10 - 1 = 9 'last char'
print(actor[len(actor) - 1])
print(actor[-1])

# Strings are IMMUTABLE [you can't change the internals (characters)]

