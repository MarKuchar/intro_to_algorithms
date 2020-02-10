""" Group Exercises """


# Problem 1: 2 x n tiles
def tiles(n):
    """
    :param n: width of 2 x n rectangle
    :return: The number of ways to fill up the 2 x n rectangle using only 2 x 1 and 1 x 2
    """
    if n <= 2:
        return n
    return tiles(n - 1) + tiles(n - 2)


# Problem 2: Triple steps
def triple_steps(n):
    """
    A child is running up a staircase with n steps and can hop
    either 1 step, 2 steps, or 3 steps at a time.
    Count how many possible ways the child can run up the stairs.
    :param n: the number of stairs
    :return: The number of possible ways the child can run up the stairs.
    """
    if n <= 2:
        return n
    if n == 3:
        return 4
    return triple_steps(n - 1) + triple_steps(n - 2) + triple_steps(n - 3)


""" group exercises 2 """


# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100

# Add one more digit to what we have so far!
# pb(2, "")
# -> pb(1, "0")
#    -> pb(0, "0" + "0") -> prints "00"
#    -> pb(0, "0" + "1") -> prints "01"
# -> pb(1, "1")
#    -> pb(1, "1" + "0") -> prints "10"
#    -> pb(1, "1" + "1") -> prints "11"
# done!


def print_binary_helper(num: int, sofar: str):
    # base case (no more digits -> print what I have so far)
    if num == 0:
        print(sofar)
    else:
        # recursive case
        print_binary_helper(num - 1, sofar + "0")
        print_binary_helper(num - 1, sofar + "1")


def print_binary(num):
    print_binary_helper(num, "")


# Write a recursive function evaluate that accepts a string
# representing a math expression and computes its value.
# - The expression will be "fully parenthesized" and will
#   consist of + and * on single-digit integers only.
# - You can use a helper function. (Do not change the original function header)
# - Recursion
#
# evaluate("7")                 -> 7
# evaluate("(2+2)"              -> 4
# evaluate("(1+(2*4))"          -> 9
# evaluate("((1+3)+((1+2)*5))") -> 19

def evaluate_helper(expr: str, i: int):
    # base case
    if expr[i].isdigit():
        return int(expr[i]), i
    else:
        # recursive case
        i += 1  # skip "("
        # left-expr
        left, i = evaluate_helper(expr, i)
        i += 1
        # operator
        op = expr[i]
        i += 1
        # right-expr
        right, i = evaluate_helper(expr, i)
        i += 1  # skip ")"
        if op == "+":
            return left + right, i
        else:
            return left * right, i


def evaluate(expr: str):
    res = evaluate_helper(expr, 0)
    return res[0]


print(evaluate("7"))
print(evaluate("(2+2)"))
print(evaluate("(1+(2*4))"))
print(evaluate("((1+3)+((1+2)*5))"))


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 00 to 99 (two digits)
# print_decimal(3)  prints from 000 to 999 (three digits)

# This is what you were supposed to do!
def print_decimal_helper(digits: int, sofar: str):
    if digits == 0:
        print(sofar)
    else:
        for i in range(10):
            print_decimal_helper(digits - 1, sofar + str(i))


def print_decimal(digits):
    print_decimal_helper(digits, "")


# This is what you did!
# def print_decimal_helper(digits, n):
#     if len(str(n)) == digits:
#         print(n)
#         print_decimal_helper(digits, n + 1)
#
#
# def print_decimal(digits):
#     n = 10 ** (digits - 1)
#     print_decimal_helper(digits, n)


""" Group Lab 2 (in-class) Exhaustive Search, Backtracking """


def permutation_helper(word: str, sofar: str):
    if len(word) == 0:
        print(sofar)
    else:
        for i in range(len(word)):
            permutation_helper(word[:i] + word[i+1:], sofar + word[i])


def permutation(word: str):
    """
    Write a recursive function permutation that accepts a string as a parameter
    and outputs all possible rearrangements of the letters in the string.
    The arrangements may be output in any order.
    example)
    permutation("park")
    output: park, pakr, pkar, prak, arpk, aprk, akrp, ...
    :param word: word to permute
    :return: display permutations of a given word
    """
    permutation_helper(word, "")


def sum_of_dice_helper(dice: int, desired_sum: int, chosen: [int]):
    if dice == 0:
        if sum(chosen) == desired_sum:
            print(chosen)
    else:
        for i in range(1, 7):
            chosen.append(i)  # choose
            sum_of_dice_helper(dice - 1, desired_sum, chosen)  # explore
            del chosen[-1]  # un-choose (remove the last elem)


def sum_of_dice(dice: int, desired_sum: int):
    """
    "Backtracking"
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.
    :param dice: the number of dice
    :param desired_sum: desired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}
    """
    sum_of_dice_helper(dice, desired_sum, [])


if __name__ == '__main__':
    permutation("park")
    sum_of_dice(2, 7)