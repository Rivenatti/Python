a = 5
b = 6

# Classic else-if statement

if b > a:
    print("b > a")
elif b == a:
    print("b == a")
else:
    print("b < a")

# Short hand if
if a > b: print('a > b')

# Short hand if...else
print('a > b') if a < b else 'a < b'

age = 16
adult = 'true' if age > 18 else 'false'
print(adult)