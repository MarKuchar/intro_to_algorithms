""" Group Lab 2 (in-class) """

def permutation_helper(word: str, prefix: str):
    if len(word) == 0:
        print(prefix)
    else:
        for i in range(len(word)):
            permutation_helper(word[:i] + word[i+1:], prefix + word[i])

def permutation(word: str):
    """
    "backtracking"
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

permutation("park")



def helper(dice: int, desired_sum: int, chosen: []):
    if dice > desired_sum or desired_sum > dice * 6:
        return
    if dice == 1:
        print(desired_sum)
        return
    else:
        for _ in range(dice):
            for a in range(1, 7):
                if desired_sum - a > 1:
                    a += 1
                return sum_of_dice(dice - 1, desired_sum - a)
                pass
def sum_of_dice(dice: int, desired_sum: int):
    """
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.

    :param dice: the number of dice
    :param desired_sum: disired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}

    """
    solution = set([])
    helper(dice, desired_sum, (), solution)
    print(solution)
    pass