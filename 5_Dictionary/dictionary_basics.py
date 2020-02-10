# lists, strings, tuples are index-based (0, 1, 2, 3, ..) linear data structure
# Dictionary: A collection of key-value pairs
# (In other languages a dictionary is called Map)
# * access its values by looking up a "key" instead of an index
# * keys must be unique (A key can be any string or number)

contacts = {
    "Cayo": "779-132-1322",
    "Martin": "213-312-3122",
    "Derrick": "123-123-3122"
}
# Acces dictionary by key to get value
print(contacts["Cayo"])

# Add a new entry (key value pair)
contacts["Leo"] = "342-123-1232"
print(contacts)

# Update a value for existing key
contacts["Cayo"] = "No phone number"
print(contacts)

# Delete an entry from dictionary
del contacts["Martin"]
print(contacts)

# Get a list of all the keys
print(list(contacts.keys()))
key_list = list(contacts.keys())
print(key_list)

# Get a list of all the values
val_list = list(contacts.values())
print(val_list)

# "in" keyword: is used to check if a list of dictionary contains a specific key.
print("John" in contacts)
print("Leo" in contacts)


