# Debug? - getting rid of the bug
# - Debugger: 'break point'

# 'break' statement: stop!
# - break out of the loop!

# ex) print numbers from the list if there is a 4 stop printing
items = [12, 1, 5, 2, 4, 12, 2, 12, 4]

for i in items:
    if i == 4:
        break
    print(i)

# ------------------------
# 'continue' statement: skip!
# - skip to the next iteration!

for i in items:
    if i == 4:
        continue
    print(i)