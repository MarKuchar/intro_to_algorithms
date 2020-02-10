# Merge Sort
# "Divide and Conquer"
# - Time Complexity: O(n logn)


def merge_sort(items: [int]):
    if len(items) <= 1:
        return items

    # divide
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # conquer (merge)
    return merge(sorted_left, sorted_right)


#   left = [1, 2, 3, 4]  right = [2, 5, 6, 8]
#           i                     j
# merged = [1, 2, 2, 3, 4, 5, 6, 8]
def merge(left: [int], right: [int]) -> [int]:
    """ O(n) """
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i == len(left):  # left list is finished
        merged += right[j:]
    else:  # right list is finished
        merged += left[i:]

    return merged