
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