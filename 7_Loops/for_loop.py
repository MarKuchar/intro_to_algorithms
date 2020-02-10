# Loops - to repeat code

# For loops are used to iterate over a given sequence.
# On each interation, the loop variable defined in the for loop will be assigned to the next value (sequence)

# Syntax:
# for __ in collection:
#     what to repeat

# Numbers (simple loop with a list)
for i in [1, 2, 3, 4, 5]:
    print(i)

# range(start, end, steps): returns a range numbers
# - range(end): 0 <=  <  end, 1 step
# - range(start, end): start <=  <  end, 1 step
# - range(start, end, steps): start <=  <  end, 1 steps
# - range

# range(1, 10) -  1, 2, 3, .., 9
# range(5) - 0, 1, 2, 3, 4
# range(2, 8, 2) - 2, 4, 6®®®
# range(10, 5, -1) - 10, 9, 8, 7, 6

for i in range(5):
    print(i)

print("-----------------")

for i in range(5, 0, -1):
    print(i)
