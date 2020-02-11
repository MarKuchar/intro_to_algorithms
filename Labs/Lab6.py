""" Primes, GCD, LCM """


def is_prime(n):
    """ Check if n is prime """
    import math
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    """ GCD of a and b """
    if a == b:
        return a
    elif a > b:
        for i in range(b, 1, -1):
            if a % i == 0 and b % i == 0:
                return i
    elif a < b:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                return i

def lcm(a, b):
    """ LCM of a and b """
    if a == b:
        return a
    elif a > b:
        for i in range(b, 1, -1):
            if a % i == 0 and b % i == 0:
                return int((a * b) / i)
    elif a < b:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                return int((a * b) / i)


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    list_prime = []
    if n < 2:
        return "Try again"
    for i in range(1, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0 and i != j:
                    break
            else:
                list_prime.append(i)

    return list_prime

