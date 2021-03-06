"""
 String, List - Level 2.0
"""


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    return string.count("hi")


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    return string.count("dog") == string.count("cat")


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    sum = 0
    for i in range(len(string) - 3):
        if string[i] + string[i+1] + string[i+3] == "coe":
            sum += 1
    return sum


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    if len(a) > len(b) or len(a) == len(b):
        return b.lower() == a[-len(b):].lower()
    else:
        return a.lower() == b[-len(a):].lower()

# return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    sum = 0
    for i in nums:
        if i % 2 == 0:
            sum += 1
    return sum


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    return max(nums) - min(nums)


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 13 or nums[i - 1] == 13 and i != 0:
            sum += 0
        else:
            sum += nums[i]

    return sum

# total = 0
# i = 0
# while i < len(nums)
#   if nums[i] == 13:
#       i +=2
#   else:
#       total += nums[i]
# return total


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    stat = True
    sum = 0
    for num in nums:
        if num == 6 and stat:
            stat = False
            continue
        if num == 7 and not stat:
            stat = True
            continue
        if stat:
            sum += num
    return sum


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    if len(nums) < 2: return False
    for i in range(len(nums) - 1):
        if nums[i+1] == 2 and nums[i] == 2:
            return True
    return False

