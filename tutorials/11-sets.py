# A set in a collection which is unordered and unindexed. In Python sets are written with curly brackets.
dataSet = {'index', 'number', 'value'}
print(dataSet) # Sets are unordered, so the items may appear in a random order

# To access items you have to loop through theand check if specified item is present
print('index' in dataSet)

# Change items is impossible

# Add new items
dataSet.add("title")
print(dataSet)

# Add multiple items
dataSet.update(["label", "tooltip"])
print(dataSet)

# Remove item
dataSet.remove("title")
print(dataSet)