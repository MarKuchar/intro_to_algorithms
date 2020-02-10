# Prime number can be divided just buy itself and 1


import math

def naive_is_prime(n):
    """ check whether n is prime or not, time complexity O(n) """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True



def is_prime(n):
    """ check whether n is prime or not, time complexity O(sqrt(n))"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# Generate a list of primes (from 2 to 100 000)
# [2, 3, 5, 7, .., 99991]



n = 100000

def generate_prime_list(n):
    prime_list = []  # create an empty list
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


print(generate_prime_list(10_000))