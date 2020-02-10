
def mrange(start, end, steps=1):
    """
    Returns a list of integers from start to end by steps
    start <= i < end, skipped by steps
    :param start:
    :param end:
    :param steps:
    :return:
    """
    list = []
    i = start
    while i < end:
        list.append(i)
        i += steps
    return list
print(mrange(1, 10))
print(mrange(1, 10, 2))


# n: arguments '*'
def nrange(*args):
    if len(args) == 1:
        return mrange(0, args[0])
    elif len(args) == 2:
        return mrange(args[0], args[1])
    elif len(args) == 3:
        return mrange(*args)
    else:
        return TypeError("Invalid Number of Arguments")  # Throw an Error by yourself
print(nrange(8))
