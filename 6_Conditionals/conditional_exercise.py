# Write a program that takes an user input for an exam mark, and prints
# the grade for that mark - according to the following scheme:
#
#
#   Mark      Grade
#   >= 90       A
#  [80-90)      B
#  [70-80)      C
#  [60-70)      D
#    < 60       F
#
#
# The square and round brackets denote closed and open intervals(range).
# A closed interval includes the number, and open interval excludes it.
# Test your program by print the mark and the grade for a number of different marks.

# TODO: Your code goes here...

exam_mark = int(input("Your exam mark is: "))

if 100 >= exam_mark >= 90:
    print("A")
elif 90 > exam_mark >= 80:
    print("B")
elif 80 > exam_mark >= 70:
    print("C")
elif 70 > exam_mark >= 60:
    print("D")
elif 60 > exam_mark >= 0:
    print("F")


