# Binary Search
# - "sorted" list of data
# - Keep comparing the item in the middle of the list to the target value
# while removing the half of the list from the search range.
# - Time Complexity: O(log n)
# In the worst case, it will take log n steps if you have n elements


def search(items, target):
    lower = 0
    upper = len(items) - 1
    steps = 0
    while lower <= upper:
        steps += 1
        mid = (lower + upper) // 2
        if items[mid] == target:
            return mid, steps
        elif items[mid] > target:
            upper = mid - 1
        elif items[mid] < target:
            lower = mid + 1
    return - 1, steps


items = [2, 4, 5, 6, 7]
print(search(items, 7))

countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador", "France", "Germany", "Hungary", "Italy", "Japan", "Korea", "Latvia",
             "Malaysia", "New Zealand", "Oman", "Poland", "Qatar", "Slovakia", "Turkey", "Uruguay", "Vietnam", "Wales", "Yemen", "Zambia"]


print(search(countries, "Slovakia"))