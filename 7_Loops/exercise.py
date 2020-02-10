# 1. Write a loop to print all even numbers fro 0 - 100 (inclusive)

i = 0
while i < 101:
    print(i); i += 2

for i in range(99, 1, -2):
    print(i)

names = ["Derrick", "Leo", "Sean", "Richard", "Douglas"]

for name in names:
    if int(len(name)) < 5:
        print(name)

# 2^0 + 2^1 + .. + 2^30  (ex. 2^1 ==> 2 ** 1)
i = 0
while i <= 31:
    number = 2 ** i; i += 1
    print(number)

result = 0
for i in range(31):
    result = 2 ** i
    print(result)
print((2 ** 31) - 1)

"""
for i in range(0, 101, 2):
    print(i)
# another way
for i in range(101):
    if i % 2 == 0:
        print(i)
# 2. Write a loop to print all odd numbers fro 0 - 100 (inclusive)

for i in range(1, 100, 2):
    print(i)
# another way
for i in range(101):
    if i % 2 == 0:
        print(i)


# Strings: a sequence of chars
for i in "Hello":
    print(i)

# lists: a sequence of items
for i in ["hello", "hola", "ahoj"]:
    print(i)

# (optional) list comprehension [ data science do for example: { x | 0 <= x < 10 }
[print(i) for i in range(10) if i % 2 == 0]
print(i)


# Exercise
# print the names that have less than 5 chars from the given list


names = ["Derrick", "Leo", "Sean", "Richard", "Douglas"]

for name in names:
    if len(name) < 5:
        print(name)


# ---------------------------------------------------

# How to write a for-loop to calculate the following
# 2^0 + 2^1 + .. + 2^30  (ex. 2^1 ==> 2 ** 1)

result = 0
for i in range(31):
    result += 2 ** i
print(result)
print((2 ** 31) - 1)

"""