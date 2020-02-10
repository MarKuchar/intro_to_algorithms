# Linear Search
# - unsorted list of data
# - search for the target in a linear manner (one by on)
# - Time Complexity: O(n)
# IN the worst case, it will take

def linear_search(items, target):
    """
    Return the index of the target in the items.
    Return -1 if the target not found
    :param items: a list of items
    :param target: the item we are searching for
    :return the index of the item in the items list
    """
    steps = 0
    for i in range(len(items)):
        steps += 1
        if items[i] == target:
            return i, steps
    return -1

items = [4, 5, 3, 2, 32, 22, 45, 2, 34, 2, 6]
print(linear_search(items, 2))