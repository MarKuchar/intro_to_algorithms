# Bubble sort
# time complexity is O(n^2)
#
# for each scan,
#   for each comparison ( two adjacent items),
#       if left item > right item:
#           "swap" two items


items = [5, 2, 1, 4, 3]


# Naive Bubble Sort --> can be improved
def bubble_sort(items):
    steps = 0
    for scan in range(len(items)):
        for j in range(len(items) - 1):  # -1 because we do not want to do the go out of order
            steps += 1
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j + 1], items[j]
    print(steps)


bubble_sort(items)
print(items)


# 1. improvement: elimination of steps we do not need to do
def bubble_sort_last_step(items):
    steps = 0
    for scan in range(len(items)):
        for j in range(len(items) - 1 - scan):  # -1 because we do not want to do the go out of order, and scan we eliminate the steps which are obviously done
            steps += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    print(steps)


bubble_sort_last_step(items)
print(items)


#  2. improvement: if we do not do any swap, the items are already sorted
def bubble_sort_fastest(items):
    steps = 0
    for scan in range(len(items)):
        is_swapped = False
        for j in range(len(items) - 1 - scan):  # -1 because we do not want to do the go out of order
            steps += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                is_swapped = True
        if not is_swapped:
            break
    print(steps)

if __name__ == '__main__':  # when we are importing and want only code
    bubble_sort_fastest(items)
    print(items)