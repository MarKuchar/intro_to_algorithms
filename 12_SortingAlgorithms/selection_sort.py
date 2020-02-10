# Selection sort
# time complexity is O(n^2)
#
# For each scan from 0 to len(items) - 1
#   find index of the minimum item (linear search)
#   swap the minimum item with items[scan]
#
# Write Selection Sort!

items = [1, 2, 3, 4, 5]


def naive_sel_sort(items):
    steps = 0
    for scan in range(len(items)):
        min_index = scan
        for i in range(scan, len(items)):
            steps += 1
            if items[i] < items[min_index]:
                min_index = i
                # swap
            items[scan], items[min_index] = items[min_index], items[scan]

    print(steps)


def improved_sel_sort(items):
    steps = 0
    for scan in range(len(items) - 1):  # we do not have to do all steps if the one is sorted
        min_index = scan
        for i in range(scan + 1, len(items)):  # we can start from the second because we already assigned min index
            steps += 1
            if items[i] < items[min_index]:
                min_index = i
        if min_index != scan:  # we did not find the smaller item
            items[scan], items[min_index] = items[min_index], items[scan]

    print(steps)

