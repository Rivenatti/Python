# String literals in python are surrounded by either single quotation marks, or double quotation marks
# 'hello' == "hello"

a = "This is a tutorial"
print(a[5]) # prints out fifth character
print(a[0:7]) # prints out substring from position 1 to 7 (not included)

b = " There is no whitespace around the text "
print(b.strip()) # The var.strip() method removes any whitespace from the beginning or the end

c = "This is a veeeeeeery long string."
print(len(c)) # The len(var) method returns the length of a string

d = "This is a TEXT"
print(d.upper()) # The var.upper() method returns the string in upper case
print(d.lower()) # The var.lower() method returns the string in lower case

e = "Rabbit"
print(e.replace("R", "H")) # The var.replace() method replaces a string with another string

f = "First message"
print(f.split(" ")) # The var.split("separator") method splits the string into substrings if it finds instances of the separator

g = "Message Reversed"
print(g[::-1])  # To reverse a string, use a slice that steps backwards