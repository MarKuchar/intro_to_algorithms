# Functions are a very convenient way to divide your code into useful blocks, make it more readable and help 'reuse' it.
# In python, functions are defined using the keyword 'def', followed by function's name.

# "input --> output", "A reusable block of code"

def print_menu():
    print("----- Menu -----")
    print("| 1. Tacos      ")
    print("| 2. Pizza      ")
    print("| 3. BBQ        ")
    print("| 4. Feijoada   ")
    print("| 5. Halusky    ")
    print("----------------")

print_menu()  # call the function

# printing menu 5x
for i in range(5):
    print_menu()  # call execute the function


def score_to_letter_grade(mark):
    if 100 >= mark >= 90:
        return "A"
    elif 90 > mark >= 80:
        return "B"
    elif 80 > mark >= 70:
        return "C"
    elif 70 > mark >= 60:
        return "D"
    elif 60 > mark >= 0:
        return "F"


print(score_to_letter_grade(82))
print(score_to_letter_grade(63))
print(score_to_letter_grade(21))
letter = score_to_letter_grade(90)
print(letter)
print(score_to_letter_grade(95))