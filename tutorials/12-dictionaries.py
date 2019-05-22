# A dictionary is a collection which is unordered, changeable and indexed. In python dictionaries are written with curly brackets, and they have keys and values.
thisDictionary = {
    "index": "1",
    "title": "Python",
    "data": "tutorial"
}

# Accessing items
item = thisDictionary["title"]
# or
item = thisDictionary.get("title")

# Loop through a dictionary
for item in thisDictionary:
    print(item)

# Loop through a dictionary values
for item in thisDictionary:
    print(thisDictionary[item])
# or
for item in thisDictionary.values():
    print(item)

# Loop through both keys and values
for x, y in thisDictionary.items():
    print(x, y)

# Adding items
thisDictionary["date"] = "today"
print(thisDictionary)

# Removing items
thisDictionary.pop("date")
print(thisDictionary)
# or
del thisDictionary["index"]
print thisDictionary

# Copy dictionary
dictCopy = thisDictionary.copy()
print(dictCopy)
# or
dictCopy = dict(thisDictionary)
print(dictCopy)