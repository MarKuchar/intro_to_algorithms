""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist):
    """
    norm = len(alist)
    for i in range(norm // 2):
        min = i
        for k in range(i + 1, norm // 2):
            if alist[k] < alist[min]: min = k
        if alist[i] != alist[min]:
            alist[i], alist[min] = alist[min], alist[i]

    for i in range(norm // 2, norm):
        max = i
        for j in range(i + 1, norm):
            if alist[j] > alist[max]: max = j
        if alist[i] != alist[max]:
            alist[i], alist[max] = alist[max], alist[i]
    return alist
    """
    mid = len(alist) // 2
    for i in range(1, mid):
        for j in range(mid - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    for l in range(mid, len(alist)):
        for s in range(mid, len(alist) - 1):
            if alist[s] < alist[s + 1]:
                alist[s + 1], alist[s] = alist[s], alist[s + 1]

    return alist

# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    list = A + B
    for num in range(len(list)):
        min = num
        for j in range(num + 1, len(list)):
            if list[j] < list[min]:
                min = j
        if list[min] != list[num]:
            list[min], list[num] = list[num], list[min]
    return list


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    for num in range(len(mylist)):
        if mylist[num] < 0:
            mylist[num] = 0
    return mylist



