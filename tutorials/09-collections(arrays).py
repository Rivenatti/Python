# List
fruits = ["apple", "banana", "pear"]
print(fruits);

# Access item
print(fruits[2])

# Change item value
fruits[0] = "pineapple"
print(fruits)

# Loop through a list
for fruit in fruits:
    print(fruit)

# Check if item exits in the list
if "pear" in fruits:
    print("Pear exists in the list")

# List length
print(len(fruits))

# Add item to list
fruits.append("orange")
print(fruits)

# Insert item at the specified index
fruits.insert(2, "cherry")
print(fruits)

# Copy a list
listCopy = list(fruits);
print(listCopy)

# Use list constructor to make a new list
newList = list(("pear", "banana", "orange"))
print(newList)

# Remove item from the list
fruits.remove("cherry")
print(fruits)

# Remove item at the specified index (or the last one if not specified)
fruits.pop()
print(fruits)

# Del keyword removes the specified index
del fruits[0]
print (fruits)

# Del keyword can delete the list completely
del listCopy