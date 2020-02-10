# Recursion

def print_star(n):
    """
    Print star (iteratively -loops)
    """
    for _ in range(n):
        print("*", end="")


def print_stars_recur(n):
    """
    Print stars (recursively without loops)
    """
    if n <= 1:
        # base case
        print("*", end="")
    else:
        # recursive case
        print("*", end="")
        print_stars_recur(n - 1)
        pass

def factiorial(n):
    """
    Print factorial of n (iteratively)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factiorial_recur(n):
    """
    Print factorial of n (recursively)
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factiorial_recur(n - 1)


def fibonnacci(n):
    """
    Returns (nth sequence) fibonacci of n (iteratively)
    1, 1, 2, 3, 5, 8, 13, 21, 34, ... nth
    O(n)
    """
    a = 1
    b = 1
    for _ in range(n - 1):  # '_' you just want to repeat
        a, b = b, a + b

    return a


def fibonnacci_recur(n):
    """
    Returns (nth sequence) fibonacci of n (recursively)
    O(2^n)
    """
    if n == 1 or n == 2:
        return 1
    return fibonnacci_recur(n - 1) + fibonnacci(n - 2)


def power(base,n):
    """
    Returns base to the power of n (iteratively)
    """
    result = 1
    for _ in range(n):
        result *= base
    return result


def power_recur(base, n):
    """
    Returns base to the power of n (recursively)
    """
    if n == 0:
        return 1
    return base * power_recur(base, n - 1)


if __name__ == '__main__':
    #  print_stars_recur(5)
    pass

