# In this lab, you will be using two searching algorithms we covered in class to
# search for a word in dictionary. Compare the performance for each algorithm.
# You will have to output the number of steps for both algorithms when used for searching
# for the same word. (case-insensitive)
# Your output should look like this. Try to search for 5 different words of your choice.
#
# ex)
# Searching for "orange"...
# Linear Search: {} steps
# Binary Search: {} steps
#
# Searching for "orangeeeeee"...
# Linear Search: no matching word found
# Binary Search: no matching word found


# Open the dictionary file and read all lines as a list of words.
with open('words') as words:
    lines = words.readlines()

# Strip off the newline character for each word.


lines = [line.strip().lower() for line in lines]


def lin_search(lines, target):
    steps = 0
    for i in range(len(lines)):
        steps += 1
        if target == lines[i]:
            return f"Linear search: {i} {steps}"
    else:
        return "no matching word found"


def bin_search(lines, target):
    lower = 0
    upper = len(lines) - 1
    steps = 0
    while lower <= upper:
        steps += 1
        mid = (lower + upper) // 2
        if lines[mid] == target:
            return f"Binary search: {mid} {steps}"
            break
        elif lines[mid] > target:
            upper = mid - 1
        elif lines[mid] < target:
            lower = mid + 1
    return f"no matching word found, {steps}"


print("Searching for 'modificatory': ")
print(lin_search(lines, "modificatory"))  # output: (17942, 117943)
print(bin_search(lines, "modificatory"))  # output: (117942, 1)

print("Searching for 'fun': ")
print(lin_search(lines, "fun"))  # output: (74194, 74195)
print(bin_search(lines, "fun"))  # output: (74194, 15)

print("Searching for 'miss': ")
print(lin_search(lines, "miss"))  # output:
print(bin_search(lines, "dog"))  # output:

print("Searching for 'orangeee': ")
print(lin_search(lines, "orangeee"))  # output: no matching word found
print(bin_search(lines, "orangeee"))  # output: no matching word found

print("Searching for 'taxi': ")
print(lin_search(lines, "taxi"))  # output: (198908, 198909)
print(bin_search(lines, "taxi"))  # output: