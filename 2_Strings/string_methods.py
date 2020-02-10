# Methods -> Functions that belong to String type
# str.method() (dot operator to call methods)
# method() -> '()' call, execute, run

city = "vancouver"

# 1. Capitalize
print(city.capitalize())  # Vancouver

# 2. Uppercase (A), Lowercase (a)
upper_city = city.upper()
print(upper_city)
lower_city = city.lower()
print(lower_city)

# 3. index: returns the index of substring (no match will return error)
#    find: returns the index of substring (no match will return -1)
print(city.index("o"))  # 4
print(city.index("cou"))  # 3 (the first index)
# print(city.index("x"))  # error
print(city.find("x"))  # -1

# 4. count certain string. count: returns the occurrences of sub-sting in string
#    * case-sensitive (0) vs case-intensive

food = "poutine donut tacos big-mac pizza"
print(food.count("o"))  # 3
print(food.count("os"))  # 1
print(food.count(" "))  # 4  "space is a character (ASCII 32)

# 5. 'in' operator: check whether some string is in another string
greeting = "hello world"
message = "hello"
print("hello" in "hello world")  # True

# 6. String validation
#    isalnum(): checks if string has alphanumeric chars (alphabets + numbers)
#    isalpha(): checks if string has alphabets (only alphabet)
#    isdigit(): checks if string has digits (only numbers)
#    isupper():
#    islower():
#    isspace(): check if string has whitespace chars
#               - space(" "), tab("\t"), newline("\n")

unit_num = "123"
street_name = "Robson"

print(unit_num.isdigit())  # True
print(street_name.isalpha())  # True



