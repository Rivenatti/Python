# Creating a function
# In Python a function is defined using the def keyword
def my_fuction():
    print("Function call")

# Calling a function
my_fuction()



# Function with parameters
def par_function(data):
    print(data)

par_function("Called paramterer in function")

# Default parameter value
def par_function(data = "This is a default data text"):
    print(data)

par_function()

print('\n')

# Passing a List as a parameter
def lists_function(list):
    for item in list:
        print item

vegetables = ['onion', 'carrot', 'cabbage']
lists_function(vegetables)